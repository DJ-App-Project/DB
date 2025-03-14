class Role:
    def __init__(self, name):
        self.name = name
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def remove_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions


class User:
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def add_role(self, role):
        self.roles.add(role)

    def remove_role(self, role):
        self.roles.discard(role)

    def has_permission(self, permission):
        for role in self.roles:
            if role.has_permission(permission):
                return True
        return False


# Example usage
admin_role = Role("admin")
admin_role.add_permission("create_user")
admin_role.add_permission("delete_user")

user_role = Role("user")
user_role.add_permission("view_content")

admin = User("admin_user")
admin.add_role(admin_role)

regular_user = User("regular_user")
regular_user.add_role(user_role)

print(admin.has_permission("create_user"))  # True
print(regular_user.has_permission("create_user"))  # False