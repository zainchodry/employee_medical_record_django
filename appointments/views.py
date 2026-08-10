from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Appointment
from .forms import AppointmentRequestForm, AppointmentManagementForm
from accounts.models import User

class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointments/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.EMPLOYEE:
            return Appointment.objects.filter(patient=user)
        return Appointment.objects.all()

class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def get_form_class(self):
        if self.request.user.role in [User.Role.DOCTOR, User.Role.ADMIN, User.Role.HR]:
            return AppointmentManagementForm
        return AppointmentRequestForm

    def form_valid(self, form):
        if self.request.user.role == User.Role.EMPLOYEE:
            form.instance.patient = self.request.user
        return super().form_valid(form)

class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    success_url = reverse_lazy('appointment_list')

    def get_form_class(self):
        if self.request.user.role in [User.Role.DOCTOR, User.Role.ADMIN, User.Role.HR]:
            return AppointmentManagementForm
        return AppointmentRequestForm