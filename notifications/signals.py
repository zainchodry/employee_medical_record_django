from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment
from .models import UserAlert

@receiver(post_save, sender=Appointment)
def notify_appointment_status(sender, instance, created, **kwargs):
    # If it's an update and the status is approved
    if not created and instance.status == Appointment.Status.APPROVED:
        UserAlert.objects.create(
            user=instance.patient,
            title="Appointment Approved",
            message=f"Your appointment on {instance.date} at {instance.time} has been approved."
        )