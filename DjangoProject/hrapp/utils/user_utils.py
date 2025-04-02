from django.contrib.auth.models import Group, User


#USER UTILS ARE FOR USER MANIPULATION ETC, LOOK FUNCTIONS FOR USERS HERE

def assign_user_to_group(username: str, group_name: str):
    """Assigns a user to a specified group, creating the group if needed."""
    try:
        user = User.objects.get(username=username)
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        user.save()
    except User.DoesNotExist:
        print(f"User '{username}' not found.")
