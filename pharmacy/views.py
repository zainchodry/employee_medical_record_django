from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from medical_records.mixins import DoctorOrAdminRequiredMixin
from medical_records.models import MedicalRecord
from .models import StockBatch, Dispensation
from .forms import DispenseForm

class InventoryListView(DoctorOrAdminRequiredMixin, ListView):
    model = StockBatch
    template_name = 'pharmacy/inventory_list.html'
    context_object_name = 'batches'
    
    def get_queryset(self):
        return StockBatch.objects.select_related('medicine').filter(quantity__gt=0).order_by('expiry_date')

class DispenseMedicineView(DoctorOrAdminRequiredMixin, CreateView):
    model = Dispensation
    form_class = DispenseForm
    template_name = 'pharmacy/dispense_form.html'
    
    def get_success_url(self):
        return reverse_lazy('record_detail', kwargs={'pk': self.kwargs['record_id']})

    def form_valid(self, form):
        # Link the dispensation to the specific medical record passed in the URL
        record = get_object_or_404(MedicalRecord, pk=self.kwargs['record_id'])
        form.instance.medical_record = record
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record'] = get_object_or_404(MedicalRecord, pk=self.kwargs['record_id'])
        return context