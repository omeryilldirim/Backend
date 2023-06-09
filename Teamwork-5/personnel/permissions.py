from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or (obj.user == request.user))
    
class IsSuperuser(permissions.IsAdminUser):

    def has_permission(self, request, view):
        return bool(request.user.is_superuser)
8
class IsRegularUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(not (request.user.is_staff or request.user.is_superuser))