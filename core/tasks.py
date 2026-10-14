from celery import shared_task


@shared_task
def health_ping():
    """Placeholder beat task so Celery beat has a schedule out of the box."""
    return {"status": "ok"}
