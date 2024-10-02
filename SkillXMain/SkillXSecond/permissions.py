from rest_framework import permissions

class IsTutor(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_tutor

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.tutor == request.user

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and request.user.is_student
        return False

class CanAddFeedback(permissions.BasePermission):
    def has_permission(self, request, view):

        return request.user.is_authenticated and request.user.is_student

    def has_object_permission(self, request, view, obj):

        return obj.students.filter(id=request.user.id).exists()
