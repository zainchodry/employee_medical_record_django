from django.urls import path
from . import views

urlpatterns = [
    path('', views.AlertListView.as_view(), name='alert_list'),
    path('<int:pk>/read/', views.mark_as_read, name='mark_alert_read'),
]