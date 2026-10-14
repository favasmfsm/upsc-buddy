import logging

from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import CADocument

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=CADocument)
def track_file_change(sender, instance: CADocument, **kwargs):
    instance._enqueue_generation = False
    if instance.pk is None:
        instance._enqueue_generation = True
        return
    try:
        previous = CADocument.objects.get(pk=instance.pk)
    except CADocument.DoesNotExist:
        instance._enqueue_generation = True
        return
    if previous.file.name != instance.file.name:
        instance._enqueue_generation = True
        instance.status = CADocument.Status.PENDING
        instance.error_message = ""


def _enqueue(document_id: int, force: bool = False):
    from .tasks import generate_questions_for_document

    try:
        generate_questions_for_document.apply_async(
            args=[document_id],
            kwargs={"force": force},
            ignore_result=True,
        )
    except Exception:
        logger.exception(
            "Failed to enqueue CA generation for document %s "
            "(is Redis/Celery running?)",
            document_id,
        )


@receiver(post_save, sender=CADocument)
def enqueue_generation(sender, instance: CADocument, created, **kwargs):
    if not getattr(instance, "_enqueue_generation", False):
        return
    doc_id = instance.pk
    transaction.on_commit(lambda: _enqueue(doc_id, force=False))
