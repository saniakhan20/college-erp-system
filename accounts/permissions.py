from rest_framework.permissions import BasePermission


class IsAdminUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "ADMIN"


class IsStudentUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "STUDENT"


class IsFacultyUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "FACULTY"