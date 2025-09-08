import os

class DatabaseConfig:
    """数据库配置类"""
    
    # 数据库连接配置
    DB_HOST = os.getenv('DB_HOST', '47.236.145.29')
    DB_PORT = os.getenv('DB_PORT', '1433')
    DB_USER = os.getenv('DB_USER', 'manager1')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '123')
    DB_NAME = os.getenv('DB_NAME', 'mydb')
    
    # SQLAlchemy 配置
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # 是否显示SQL语句
