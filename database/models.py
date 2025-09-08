from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 创建 db 实例，避免循环导入
db = SQLAlchemy()

# 这个文件将包含所有的数据库模型定义
# 对应数据库中的三个表：user, user_auth, user_token

class User(db.Model):
    """用户表模型 - 对应数据库中的 user 表"""
    __tablename__ = 'user'
    
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    point = db.Column(db.BigInteger, default=0, nullable=False)
    
    # 关联关系
    auth = db.relationship('UserAuth', backref='user', uselist=False, cascade='all, delete-orphan')
    token = db.relationship('UserToken', backref='user', uselist=False, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.id}>'


class UserAuth(db.Model):
    """用户认证表模型 - 对应数据库中的 user_auth 表"""
    __tablename__ = 'user_auth'
    
    id = db.Column(db.BigInteger, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<UserAuth {self.username}>'


class UserToken(db.Model):
    """用户令牌表模型 - 对应数据库中的 user_token 表"""
    __tablename__ = 'user_token'
    
    id = db.Column(db.BigInteger, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    token = db.Column(db.String(32), nullable=False)
    
    def __repr__(self):
        return f'<UserToken {self.token[:8]}...>'
