from rest_framework import permissions


class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())

        if user.is_staff:
            if user.has_perm("products.view_product"):
                return True
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user