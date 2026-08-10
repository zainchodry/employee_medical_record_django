from django.db import models
from medical_records.models import MedicalRecord

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class StockBatch(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='batches')
    batch_number = models.CharField(max_length=50, unique=True)
    quantity = models.PositiveIntegerField(default=0)
    expiry_date = models.DateField()
    supplier = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.medicine.name} (Batch: {self.batch_number}) - Qty: {self.quantity}"

class Dispensation(models.Model):
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, related_name='dispensed_medicines')
    stock_batch = models.ForeignKey(StockBatch, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField()
    date_dispensed = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically deduct from inventory when dispensing
        if self._state.adding:
            self.stock_batch.quantity -= self.quantity
            self.stock_batch.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dispensed {self.quantity} of {self.stock_batch.medicine.name}"