from django import forms
from .models import MedicalRecord


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord

        fields = [
            'employee',
            'diagnosis',
            'symptoms',
            'prescription',
            'prescription_file',
            'lab_notes',
            'lab_report_file',
            'status',
            'blood_pressure',
            'temperature_f',
            'follow_up_date',
        ]

        widgets = {
            'employee': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Select employee',
            }),

            'diagnosis': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter diagnosis',
            }),

            'symptoms': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter symptoms',
            }),

            'prescription': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter prescription details',
            }),

            'prescription_file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.jpg,.jpeg,.png',
            }),

            'lab_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter laboratory notes',
            }),

            'lab_report_file': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx,.jpg,.jpeg,.png',
            }),

            'status': forms.Select(attrs={
                'class': 'form-select',
            }),

            'blood_pressure': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 120/80',
            }),

            'temperature_f': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 98.6',
                'step': '0.1',
                'min': '90',
                'max': '110',
            }),

            'follow_up_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }
