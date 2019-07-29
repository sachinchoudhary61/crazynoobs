
def autherize(auth, user_role, role):
    if auth == True:
        if user_role == role:
            return True
        else:
            return False, "wrongUser"
    else:
        return False, "notLogin"
