from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from medical_records.models import MedicalRecord
from appointments.models import Appointment
from notifications.models import UserAlert

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    context = {
        'total_records': MedicalRecord.objects.filter(employee=user).count() if user.role == 'EMPLOYEE' else MedicalRecord.objects.count(),
        'total_appointments': Appointment.objects.filter(patient=user).count() if user.role == 'EMPLOYEE' else Appointment.objects.count(),
        'pending_appointments': Appointment.objects.filter(status='PENDING').count() if user.role != 'EMPLOYEE' else Appointment.objects.filter(patient=user, status='PENDING').count(),
        'unread_alerts': UserAlert.objects.filter(user=user, is_read=False).count(),
        'recent_records': (MedicalRecord.objects.filter(employee=user) if user.role == 'EMPLOYEE' else MedicalRecord.objects.all()).select_related('employee', 'doctor')[:5],
        'recent_appointments': (Appointment.objects.filter(patient=user) if user.role == 'EMPLOYEE' else Appointment.objects.all()).select_related('patient', 'doctor')[:5],
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def profile_view(request):
    # View logic is simple; just render the template with the request.user
    return render(request, 'accounts/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile_update.html', context)