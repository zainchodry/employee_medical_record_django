from django.urls import path
from . import views

urlpatterns = [
    path('', views.MedicalRecordListView.as_view(), name='record_list'),
    path('new/', views.MedicalRecordCreateView.as_view(), name='record_create'),
    path('<int:pk>/', views.MedicalRecordDetailView.as_view(), name='record_detail'),
    path('<int:pk>/edit/', views.MedicalRecordUpdateView.as_view(), name='record_update'),
]