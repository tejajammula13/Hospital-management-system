from rest_framework.permissions import BasePermission

# Admin Permission
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and (
                request.user.is_superuser
                or request.user.is_staff
                or request.user.groups.filter(name='Admin').exists()
            )
        )

# Doctor Permission
class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.groups.filter(name='Doctor').exists()
        )

# Receptionist Permission
class IsReceptionist(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.groups.filter(name='Receptionist').exists()
        )

#COMBINED PERMISSIONS 

# Admin OR Doctor OR Receptionist
class IsAdminOrDoctorOrReceptionist(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user
            and (
                user.is_superuser
                or user.is_staff
                or user.groups.filter(
                    name__in=['Admin', 'Doctor', 'Receptionist']
                ).exists()
            )
        )

# Admin OR Receptionist
class IsAdminOrReceptionist(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user
            and (
                user.is_superuser
                or user.is_staff
                or user.groups.filter(name__in=['Admin', 'Receptionist']).exists()
            )
        )
