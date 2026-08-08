from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class MedicalRecord(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active Treatment'
        RESOLVED = 'RESOLVED', 'Resolved'
        UNDER_OBSERVATION = 'UNDER_OBSERVATION', 'Under Observation'

    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='medical_records',
        limit_choices_to={'role': 'EMPLOYEE'}
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='diagnosed_records'
    )
    
    diagnosis = models.CharField(max_length=255)
    symptoms = models.TextField()
    prescription = models.TextField(blank=True, null=True)
    lab_notes = models.TextField(blank=True, null=True)
    
    # File Attachments
    prescription_file = models.FileField(
        upload_to='prescriptions/%Y/%m/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])]
    )
    lab_report_file = models.FileField(
        upload_to='lab_reports/%Y/%m/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])]
    )
    
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.ACTIVE
    )
    blood_pressure = models.CharField(max_length=15, blank=True, null=True)
    temperature_f = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    
    record_date = models.DateField(auto_now_add=True)
    follow_up_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-record_date', '-created_at']

    def __str__(self):
        return f"{self.employee.email} - {self.diagnosis}"
