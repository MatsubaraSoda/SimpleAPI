# 数据库操作函数
# 这个文件将包含所有的数据库CRUD操作

from database.models import db, User, UserAuth, UserToken
from module.password_hash import password_hash
from module.generate_token import generate_token

def create_tables():
    """创建所有数据库表"""
    db.create_all()

def drop_tables():
    """删除所有数据库表"""
    db.drop_all()

def init_database():
    """初始化数据库"""
    create_tables()

def register_user_to_db(username, password):
    """
    注册用户到数据库
    在 user, user_auth, user_token 三个表中创建相应数据
    
    Args:
        username (str): 用户名
        password (str): 密码
        
    Returns:
        dict: 包含注册结果的字典
    """
    try:
        # 检查用户名是否已存在
        existing_auth = UserAuth.query.filter_by(username=username).first()
        if existing_auth:
            return {
                "status": "error",
                "message": "用户名已存在"
            }
        
        # 1. 创建 user 记录
        user = User(point=0)
        db.session.add(user)
        db.session.flush()  # 获取自增ID
        
        # 2. 加密密码
        bcrypt_hash, argon2_hash = password_hash(password)
        
        # 3. 创建 user_auth 记录
        user_auth = UserAuth(
            id=user.id,  # 使用相同的ID作为主键和外键
            username=username,
            password_hash=argon2_hash
        )
        db.session.add(user_auth)
        
        # 4. 生成token
        token = generate_token()
        
        # 5. 创建 user_token 记录
        user_token = UserToken(
            id=user.id,  # 使用相同的ID作为主键和外键
            token=token
        )
        db.session.add(user_token)
        
        # 6. 提交事务
        db.session.commit()
        
        return {
            "status": "success",
            "message": "注册成功",
            "user_id": user.id,
            "username": username,
            "token": token
        }
        
    except Exception as e:
        db.session.rollback()  # 回滚事务
        return {
            "status": "error",
            "message": f"注册失败: {str(e)}"
        }

def get_user_by_username(username):
    """根据用户名获取用户信息"""
    return UserAuth.query.filter_by(username=username).first()

def get_user_by_token(token):
    """根据token获取用户信息"""
    user_token = UserToken.query.filter_by(token=token).first()
    if user_token:
        return user_token.user
    return None

def login_user(username, password):
    """
    用户登录验证
    
    Args:
        username (str): 用户名
        password (str): 密码原文
        
    Returns:
        dict: 包含登录结果的字典
    """
    try:
        # 1. 根据用户名查找用户认证信息
        user_auth = UserAuth.query.filter_by(username=username).first()
        if not user_auth:
            return {
                "status": "error",
                "message": "用户名不存在"
            }
        
        # 2. 验证密码
        from argon2 import PasswordHasher
        ph = PasswordHasher()
        
        try:
            # 验证密码哈希
            ph.verify(user_auth.password_hash, password)
        except Exception:
            return {
                "status": "error",
                "message": "密码错误"
            }
        
        # 3. 获取用户信息
        user = User.query.get(user_auth.id)
        if not user:
            return {
                "status": "error",
                "message": "用户数据异常"
            }
        
        # 4. 生成新的token
        token = generate_token()
        
        # 5. 更新或创建user_token记录
        user_token = UserToken.query.filter_by(id=user.id).first()
        if user_token:
            # 更新现有token
            user_token.token = token
        else:
            # 创建新token记录
            user_token = UserToken(id=user.id, token=token)
            db.session.add(user_token)
        
        # 6. 提交事务
        db.session.commit()
        
        # 7. 返回用户数据和token
        return {
            "status": "success",
            "message": "登录成功",
            "user": {
                "id": user.id,
                "point": user.point
            },
            "token": token
        }
        
    except Exception as e:
        db.session.rollback()
        return {
            "status": "error",
            "message": f"登录失败: {str(e)}"
        }
