from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name='appointment_list'),
    path('request/', views.AppointmentCreateView.as_view(), name='appointment_create'),
    path('<int:pk>/edit/', views.AppointmentUpdateView.as_view(), name='appointment_update'),
]