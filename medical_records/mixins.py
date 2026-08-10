from django.contrib.auth.mixins import AccessMixin
from accounts.models import User

class DoctorOrAdminRequiredMixin(AccessMixin):
    """Verify that the current user is a Doctor, HR, or Admin."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
            
        allowed_roles = [User.Role.DOCTOR, User.Role.ADMIN, User.Role.HR]
        if request.user.role not in allowed_roles:
            return self.handle_no_permission()
            
        return super().dispatch(request, *args, **kwargs)