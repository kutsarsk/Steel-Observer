from django.core.exceptions import PermissionDenied


class PermissionMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not (self.request.user.is_staff or self.request.user.is_superuser):
            raise PermissionDenied
        return obj


class SuperPermissionMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied
        return obj
