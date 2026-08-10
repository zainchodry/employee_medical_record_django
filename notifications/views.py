from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import UserAlert

class AlertListView(LoginRequiredMixin, ListView):
    model = UserAlert
    template_name = 'notifications/alert_list.html'
    context_object_name = 'alerts'

    def get_queryset(self):
        return UserAlert.objects.filter(user=self.request.user)

@login_required
def mark_as_read(request, pk):
    alert = get_object_or_404(UserAlert, pk=pk, user=request.user)
    alert.is_read = True
    alert.save()
    return redirect(reverse('alert_list'))