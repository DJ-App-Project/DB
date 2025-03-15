from pymongo import MongoClient
from bson.objectid import ObjectId

# Povezava na MongoDB
client = MongoClient("mongodb://djadmin:DJsuggester2025!@mongodbitk.duckdns.org:27017/")
db = client["DJSuggestionsDB"]

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

# Inicializacija podatkov
def initialize_data():
    # Ustvarjanje vlog
    roles = [
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5b5"), "name": "admin", "description": "Administrator role", "permissions": ["create_user", "delete_user"]},
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5b6"), "name": "user", "description": "User role", "permissions": ["view_content"]}
    ]
    db.roles.insert_many(roles)

    # Ustvarjanje dovoljenj
    permissions = [
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5b7"), "name": "create_user", "description": "Permission to create a user"},
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5b8"), "name": "delete_user", "description": "Permission to delete a user"},
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5b9"), "name": "view_content", "description": "Permission to view content"}
    ]
    db.permissions.insert_many(permissions)

    # Povezovanje dovoljenj z vlogami
    role_permissions = [
        {"roleId": ObjectId("60d5ec49f8d2f5a5d8b5b5b5"), "permissionId": ObjectId("60d5ec49f8d2f5a5d8b5b5b7")},
        {"roleId": ObjectId("60d5ec49f8d2f5a5d8b5b5b5"), "permissionId": ObjectId("60d5ec49f8d2f5a5d8b5b5b8")},
        {"roleId": ObjectId("60d5ec49f8d2f5a5d8b5b5b6"), "permissionId": ObjectId("60d5ec49f8d2f5a5d8b5b5b9")}
    ]
    db.role_permissions.insert_many(role_permissions)

    # Ustvarjanje uporabnikov in dodeljevanje vlog
    users = [
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5ba"), "username": "admin_user", "roles": ["admin"]},
        {"_id": ObjectId("60d5ec49f8d2f5a5d8b5b5bb"), "username": "regular_user", "roles": ["user"]}
    ]
    db.users.insert_many(users)

    user_roles = [
        {"userId": ObjectId("60d5ec49f8d2f5a5d8b5b5ba"), "roleId": ObjectId("60d5ec49f8d2f5a5d8b5b5b5")},
        {"userId": ObjectId("60d5ec49f8d2f5a5d8b5b5bb"), "roleId": ObjectId("60d5ec49f8d2f5a5d8b5b5b6")}
    ]
    db.user_roles.insert_many(user_roles)

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

# Inicializacija podatkov
initialize_data()

# Primer uporabe
admin_id = db.users.find_one({"username": "admin_user"})["_id"]
regular_user_id = db.users.find_one({"username": "regular_user"})["_id"]

create_user(admin_id)  
create_user(regular_user_id)  

delete_user(admin_id) 
delete_user(regular_user_id)  

view_content(admin_id)  
view_content(regular_user_id)