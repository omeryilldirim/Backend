from rest_framework.permissions import BasePermission, SAFE_METHODS 


# permission for car viewset
class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_staff
        )
    

# permission for reservation viewset
class IsOwnerOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_staff or
            obj.user.id == request.user.id
        )