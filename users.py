USER_PERMISSION_RULE = "reader_only"


def create_user(username, role="reader"):
    user = {
        "username": username,
        "role": role
    }
    return user


def describe_user_rule():
    return "当前用户权限规则：" + USER_PERMISSION_RULE