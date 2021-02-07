from celery import shared_task

@shared_task(
    #autoretry_for=(Page.DoesNotExist,),
    default_retry_delay=20,
    max_retries=5
)
def update_counter(obj_id):
    from .models import Page

    Page.objects.get(id=obj_id).update_counter()
