from django.contrib.auth.models import Group
from rest_framework import permissions


def is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class HasGroupPermission(permissions.BasePermission):
    """
    Ensure user is in required groups.
    """

    def has_permission(self, request, view):
        # Get a mapping of methods -> required group.
        required_groups_mapping = getattr(view, "required_groups", {})
        # Determine the required groups for this particular request method.
        required_groups = required_groups_mapping.get(request.method, [])
        test = ""
        user1 = str(request.user)
        for data in required_groups:
            data1 = str(data)
            if user1.find(data1.upper()) == 0:
                test = data in required_groups
                break
            else:
                test = False
                part = all([is_in_group(request.user, group_name) if group_name != "__all__" else True for group_name in
                            required_groups]) or (request.user and request.user.is_staff)
                if part is True:
                    test = True

        # Return True if the user has all the required groups or is staff.
        return test
