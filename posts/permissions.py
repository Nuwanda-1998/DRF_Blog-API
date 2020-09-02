from rest_framework import permissions



'Create Custom Permissions to allow all user see the post but only the owner can edit it'
class IsAuthorOrReadOnly(permissions.BasePermission):




    def has_object_permission(self, request, view, obj):
        'Read-only permissions are allowed for any request'
        if request.method in permissions.SAFE_METHODS:
            return True
        
        
        'Write permissions are only allowed to the author of a post'
        return obj.author == request.user
    