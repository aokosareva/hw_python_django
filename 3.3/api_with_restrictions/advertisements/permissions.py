from rest_framework.permissions import BasePermission


class IsOwnerForDraftOrManipulations(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE'] or obj.is_draft():
            return request.user == obj.creator

        return True
