from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email Address'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'role': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Create Password'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'date_of_birth',
            'gender',
            'marital_status',
            'address',
            'department',
            'designation',
            'blood_group',
            'emergency_contact_name',
            'emergency_contact_phone',
        ]

        widgets = {
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),

            'marital_status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter Full Address'
            }),

            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Department'
            }),

            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Designation'
            }),

            'blood_group': forms.Select(attrs={
                'class': 'form-select'
            }),

            'emergency_contact_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emergency Contact Name'
            }),

            'emergency_contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Emergency Contact Phone'
            }),
        }