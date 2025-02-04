from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class AdminBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.is_staff and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

class UserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if not user.is_staff and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
