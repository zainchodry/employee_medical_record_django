from django.contrib import admin
from .models import MedicalRecord

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'diagnosis', 'doctor', 'status', 'record_date')
    list_filter = ('status', 'record_date')
    search_fields = ('employee__email', 'diagnosis', 'doctor__email')
    readonly_fields = ('created_at', 'updated_at')