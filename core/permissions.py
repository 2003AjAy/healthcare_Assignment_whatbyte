from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of a Patient to edit/delete it.
    """

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request (GET) if desired.
        if request.method in permissions.SAFE_METHODS:
            return True
        # instance must have an `owner` attribute
        return getattr(obj, 'owner', None) == request.user
