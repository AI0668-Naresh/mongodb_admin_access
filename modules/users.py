from __init__ import client

def list_all_users(client):
    
    db = client['admin']
    users = db.command('usersInfo')
    if 'users' in users:
        for user in users['users']:
            print(f"Username: {user['user']}, Roles: {user['roles']}")
    else:
        print("No users found.")

def create_user(user, pwd, client):
    
    db = client['admin']
    db.command("createUser", user, pwd=pwd, roles=[])

def drop_user(user, client):
    
    db = client['admin']
    db.command("dropUser", user)

def add_role(user, role, client):
    
    db = client['admin']
    db.command("grantRolesToUser", user, roles=[role])

def remove_role(user, role, client):
    
    db = client['admin']
    db.command("revokeRolesFromUser", user, roles=[role])

def create_role(role, client):
    
    db = client['admin']
    db.command("createRole", role, privileges=[], roles=[])

def drop_role( role, client,):
    
    db = client['admin']
    db.command("dropRole", role)

def list_all_roles(client):
    
    db = client['admin']
    roles = db.command('rolesInfo')
    print(roles)
    if 'roles' in roles:
        for role in roles['roles']:
            print(f"Role: {role['role']}, Privileges: {role['privileges']}")
    else:
        print("No roles found.")

def add_privilege(role, privilege, client):
    
    db = client['admin']
    db.command("grantPrivilegesToRole", role, privileges=[privilege])

def remove_privilege( role, privilege,client):
    
    db = client['admin']
    db.command("revokePrivilegesFromRole", role, privileges=[privilege])
