from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MedicalRecord
from .forms import MedicalRecordForm
from .mixins import DoctorOrAdminRequiredMixin
from accounts.models import User

class MedicalRecordListView(LoginRequiredMixin, ListView):
    model = MedicalRecord
    template_name = 'medical_records/record_list.html'
    context_object_name = 'records'

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.EMPLOYEE:
            return MedicalRecord.objects.filter(employee=user)
        # Doctors and Admins see all records
        return MedicalRecord.objects.select_related('employee', 'doctor').all()

class MedicalRecordDetailView(LoginRequiredMixin, DetailView):
    model = MedicalRecord
    template_name = 'medical_records/record_detail.html'
    context_object_name = 'record'

    def get_queryset(self):
        user = self.request.user
        if user.role == User.Role.EMPLOYEE:
            return MedicalRecord.objects.filter(employee=user)
        return MedicalRecord.objects.all()

class MedicalRecordCreateView(DoctorOrAdminRequiredMixin, CreateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medical_records/record_form.html'
    success_url = reverse_lazy('record_list')

    def form_valid(self, form):
        # Automatically set the logged-in doctor as the creator
        form.instance.doctor = self.request.user
        return super().form_valid(form)

class MedicalRecordUpdateView(DoctorOrAdminRequiredMixin, UpdateView):
    model = MedicalRecord
    form_class = MedicalRecordForm
    template_name = 'medical_records/record_form.html'
    
    def get_success_url(self):
        return reverse_lazy('record_detail', kwargs={'pk': self.object.pk})