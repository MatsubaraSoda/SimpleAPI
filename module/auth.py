from database.operations import register_user_to_db, login_user

def register_user(username, password):
    """
    用户注册功能
    
    Args:
        username (str): 用户名
        password (str): 密码
        
    Returns:
        dict: 包含注册结果的响应数据
    """
    # 调用数据库操作函数
    return register_user_to_db(username, password)

def login_user_auth(username, password):
    """
    用户登录功能
    
    Args:
        username (str): 用户名
        password (str): 密码
        
    Returns:
        dict: 包含登录结果的响应数据
    """
    # 调用数据库操作函数
    return login_user(username, password)
