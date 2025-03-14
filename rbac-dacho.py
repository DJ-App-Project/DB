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


# Definirajte vloge in dovoljenja
admin_role = Role("admin")
admin_role.add_permission("create_user")
admin_role.add_permission("delete_user")

user_role = Role("user")
user_role.add_permission("view_content")

# Ustvarite uporabnike in jim dodelite vloge
admin = User("admin_user")
admin.add_role(admin_role)

regular_user = User("regular_user")
regular_user.add_role(user_role)

# Preverite dovoljenja pred izvajanjem akcij
def create_user(user):
    if user.has_permission("create_user"):
        print(f"{user.username} can create a user.")
    else:
        print(f"{user.username} cannot create a user.")

def delete_user(user):
    if user.has_permission("delete_user"):
        print(f"{user.username} can delete a user.")
    else:
        print(f"{user.username} cannot delete a user.")

def view_content(user):
    if user.has_permission("view_content"):
        print(f"{user.username} can view content.")
    else:
        print(f"{user.username} cannot view content.")

# Primer uporabe
create_user(admin)  
create_user(regular_user)  

delete_user(admin) 
delete_user(regular_user)  

view_content(admin)  
view_content(regular_user)  