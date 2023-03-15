from rest_framework.permissions import BasePermission

from application.access_control.api.permissions import (
    check_post_permission,
    check_object_permission,
)
from application.access_control.services.roles_permissions import Permissions
from application.core.models import Product


class UserHasApiConfigurationPermission(BasePermission):
    def has_permission(self, request, view):
        return check_post_permission(
            request, Product, "product", Permissions.Api_Configuration_Create
        )

    def has_object_permission(self, request, view, obj):
        return check_object_permission(
            request,
            obj,
            Permissions.Api_Configuration_View,
            Permissions.Api_Configuration_Edit,
            Permissions.Api_Configuration_Delete,
        )
