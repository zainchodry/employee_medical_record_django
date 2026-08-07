from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from . managers import CustomUserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        HR = 'HR', _('HR')
        DOCTOR = 'DOCTOR', _('Doctor')
        EMPLOYEE = 'EMPLOYEE', _('Employee')

    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Basic Info
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Employee Info
    department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    
    # Medical & Emergency Info
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.email}"