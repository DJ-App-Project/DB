from pymongo import MongoClient
from bson.objectid import ObjectId

# Povezava na MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["rbac_db"]

class Role:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.permissions = set()

    def add_permission(self, permission):
        self.permissions.add(permission)

    def remove_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions

    def save_to_db(self):
        role_data = {
            "name": self.name,
            "description": self.description,
            "permissions": list(self.permissions)
        }
        db.roles.insert_one(role_data)

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

    def save_to_db(self):
        user_data = {
            "username": self.username,
            "roles": [role.name for role in self.roles]
        }
        db.users.insert_one(user_data)

# Definirajte vloge in dovoljenja
admin_role = Role("admin", "Administrator role")
admin_role.add_permission("create_user")
admin_role.add_permission("delete_user")
admin_role.save_to_db()

user_role = Role("user", "User role")
user_role.add_permission("view_content")
user_role.save_to_db()

# Ustvarite uporabnike in jim dodelite vloge
admin = User("admin_user")
admin.add_role(admin_role)
admin.save_to_db()

regular_user = User("regular_user")
regular_user.add_role(user_role)
regular_user.save_to_db()

# Preverite dovoljenja pred izvajanjem akcij
def has_permission(user_id, permission_name):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return False

    role_names = user["roles"]
    roles = db.roles.find({"name": {"$in": role_names}})
    for role in roles:
        if permission_name in role["permissions"]:
            return True
    return False

def create_user(user_id):
    if has_permission(user_id, "create_user"):
        print(f"User with ID {user_id} can create a user.")
    else:
        print(f"User with ID {user_id} cannot create a user.")

def delete_user(user_id):
    if has_permission(user_id, "delete_user"):
        print(f"User with ID {user_id} can delete a user.")
    else:
        print(f"User with ID {user_id} cannot delete a user.")

def view_content(user_id):
    if has_permission(user_id, "view_content"):
        print(f"User with ID {user_id} can view content.")
    else:
        print(f"User with ID {user_id} cannot view content.")

# Primer uporabe
admin_id = db.users.find_one({"username": "admin_user"})["_id"]
regular_user_id = db.users.find_one({"username": "regular_user"})["_id"]

create_user(admin_id)  
create_user(regular_user_id)  

delete_user(admin_id) 
delete_user(regular_user_id)  

view_content(admin_id)  
view_content(regular_user_id)