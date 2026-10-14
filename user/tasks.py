from celery import shared_task


@shared_task
def noop_user_task():
    """Reserved for future auth-related background jobs."""
    return {"status": "ok"}
