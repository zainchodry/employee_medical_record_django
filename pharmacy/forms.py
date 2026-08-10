from django import forms
from .models import Dispensation, StockBatch
from django.core.exceptions import ValidationError

class DispenseForm(forms.ModelForm):
    class Meta:
        model = Dispensation
        fields = ['stock_batch', 'quantity', 'notes']
        widgets = {
            'stock_batch': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show batches that have stock and are not expired
        self.fields['stock_batch'].queryset = StockBatch.objects.filter(quantity__gt=0)

    def clean(self):
        cleaned_data = super().clean()
        batch = cleaned_data.get('stock_batch')
        qty = cleaned_data.get('quantity')
        
        if batch and qty and qty > batch.quantity:
            raise ValidationError(f"Only {batch.quantity} units available in this batch.")
        return cleaned_data