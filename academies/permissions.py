from rest_framework.permissions import BasePermission

from academies.models import AcademyMembership
from academies.utils import get_membership, require_academy

STAFF_ROLES = {
    AcademyMembership.Role.ADMIN,
    AcademyMembership.Role.STAFF,
}


class IsAcademyStaffOrSuperuser(BasePermission):
    """
    Allow academy admin/staff for the current X-Academy-Slug tenant,
    or any Django superuser.
    """

    message = "Academy admin or staff access required."

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_superuser:
            # Still require a valid academy header so writes stay tenant-scoped.
            require_academy(request)
            return True
        academy = require_academy(request)
        membership = get_membership(user, academy)
        return membership is not None and membership.role in STAFF_ROLES


class IsAcademyAdminOrSuperuser(BasePermission):
    """
    Allow academy admin for the current X-Academy-Slug tenant,
    or any Django superuser.
    """

    message = "Academy admin access required."

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_superuser:
            require_academy(request)
            return True
        academy = require_academy(request)
        membership = get_membership(user, academy)
        return (
            membership is not None
            and membership.role == AcademyMembership.Role.ADMIN
        )
