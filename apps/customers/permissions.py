from rest_framework import permissions


class AllowCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return True

        return bool(request.user and request.user.is_authenticated)
