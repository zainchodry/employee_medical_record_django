from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.InventoryListView.as_view(), name='inventory_list'),
    path('record/<int:record_id>/dispense/', views.DispenseMedicineView.as_view(), name='dispense_medicine'),
]