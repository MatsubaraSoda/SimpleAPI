from flask import Flask, request, jsonify
import os
from module.validator import validate_arithmetic_expression, validate_table_request
from module.calculator import calculate_expression
from module.generate_table import generate_table_data
from module.password_hash import password_hash
from module.generate_token import generate_token
from module.auth import register_user, login_user_auth

# 导入数据库相关
from database.models import db
from database.operations import init_database

app = Flask(__name__)

# 配置远程 MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://manager1:123@47.236.145.29:1433/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db.init_app(app)

# 添加 CORS 支持
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# 配置常量
API_VERSION = "1.0.0"
DEFAULT_PORT = 5000


@app.route("/")
def home():
    """首页路由"""
    # 检查数据库连接状态
    db_status = "disconnected"
    try:
        with db.engine.connect() as connection:
            connection.execute(db.text('SELECT 1'))
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return jsonify(
        {
            "message": "SimpleAPI - 无数据库依赖的实时计算API服务",
            "version": API_VERSION,
            "database_status": db_status,
            "apis": [
                {
                    "endpoint": "/calculate",
                    "method": "POST",
                    "description": "计算算术表达式",
                    "example": 'POST /calculate with JSON: {"expression": "2+3*4"}',
                },
                {
                    "endpoint": "/generate-table",
                    "method": "POST",
                    "description": "生成随机数据表格",
                    "example": 'POST /generate-table with JSON: {"rows": 10}',
                },
                {
                    "endpoint": "/password-hash",
                    "method": "POST",
                    "description": "生成密码哈希值",
                    "example": 'POST /password-hash with JSON: {"password": "mypassword"}',
                },
                {
                    "endpoint": "/generate-token",
                    "method": "GET",
                    "description": "生成安全随机token",
                    "example": 'GET /generate-token',
                }
            ],
        }
    )


@app.route("/calculate", methods=["POST"])
def calculate():
    """计算表达式API"""
    try:
        # 获取表达式参数
        expression = ""
        
        # 检查是否为JSON请求
        if request.is_json:
            try:
                expression = request.json.get("expression", "")
            except Exception:
                return jsonify({"error": "请求格式错误，请使用JSON格式"}), 400
        else:
            expression = request.form.get("expression", "")

        # 验证输入
        is_valid, error_message = validate_arithmetic_expression(expression)
        if not is_valid:
            return jsonify({"expression": expression, "error": error_message}), 400

        # 计算表达式
        result, status_code = calculate_expression(expression)
        return jsonify(result), status_code

    except Exception as e:
        return jsonify({"error": f"请求处理失败: {str(e)}"}), 500


@app.route("/generate-table", methods=["POST"])
def generate_table():
    """生成随机数据表格API"""
    try:
        # 获取请求数据
        if request.is_json and request.json is not None:
            data = request.json
        else:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "请求格式错误，请使用JSON格式",
                    "details": "请求体必须是有效的JSON格式"
                }
            }), 400
        
        # 验证参数
        is_valid, error_message = validate_table_request(data)
        if not is_valid:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": error_message,
                    "details": "请检查请求参数格式和范围"
                }
            }), 400
        
        # 生成数据
        rows = data.get('rows')
        result = generate_table_data(rows)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "error": {
                "code": 500,
                "message": "请求处理失败",
                "details": str(e)
            }
        }), 500


@app.route("/password-hash", methods=["POST"])
def password_hash_api():
    """密码哈希生成API"""
    try:
        # 获取请求数据
        if request.is_json and request.json is not None:
            data = request.json
        else:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "请求格式错误，请使用JSON格式",
                    "details": "请求体必须是有效的JSON格式"
                }
            }), 400
        
        # 获取密码参数
        password = data.get("password")
        if not password:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "缺少必需参数",
                    "details": "请求中必须包含 'password' 字段"
                }
            }), 400
        if type(password) != str:
            return jsonify({
                "error": {
                    "code": 400,
                    "message": "密码格式错误，请使用字符串",
                    "details": "请求中必须包含 'password' 字段"
                }
            }), 400
        
        # 生成哈希值
        bcrypt_hash, argon2_hash = password_hash(password)
        
        # 返回结果
        return jsonify({
            "bcrypt_hash": bcrypt_hash.decode('utf-8'),
            "argon2_hash": argon2_hash
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": {
                "code": 500,
                "message": "请求处理失败",
                "details": str(e)
            }
        }), 500


@app.route("/generate-token", methods=["GET"])
def generate_token_api():  # 改为不同的函数名
    """生成token API"""
    try:
        token = generate_token()  # 这里调用导入的函数
        return token, 200
    except Exception as e:
        return f"Token生成失败: {str(e)}", 500

@app.route("/auth/register", methods=["POST"])
def register():
    """注册API"""
    try:
        # 获取请求数据
        if request.is_json and request.json is not None:
            data = request.json
        else:
            return jsonify({
                "status": "error",
                "message": "请求格式错误，请使用JSON格式"
            }), 400
        
        # 获取必需参数
        username = data.get("username")
        password = data.get("password")
        
        # 检查必需参数
        if not username or not password:
            return jsonify({
                "status": "error",
                "message": "缺少必需参数username或password"
            }), 400
        
        # 调用注册功能
        result = register_user(username, password)
        
        if result["status"] == "success":
            return jsonify(result), 200
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"注册失败: {str(e)}"
        }), 500
    
@app.route("/auth/login", methods=["POST"])
def login():
    """登录API"""
    try:
        # 获取请求数据
        if request.is_json and request.json is not None:
            data = request.json
        else:
            return jsonify({
                "status": "error",
                "message": "请求格式错误，请使用JSON格式"
            }), 400
        
        # 获取必需参数
        username = data.get("username")
        password = data.get("password")
        
        # 检查必需参数
        if not username or not password:
            return jsonify({
                "status": "error",
                "message": "缺少必需参数username或password"
            }), 400
        
        # 调用登录功能
        result = login_user_auth(username, password)
        
        if result["status"] == "success":
            return jsonify(result), 200
        else:
            return jsonify(result), 401  # 使用401状态码表示认证失败
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"登录失败: {str(e)}"
        }), 500

@app.route("/auth/verify", methods=["POST"])
def verify():
    """验证Token并返回用户数据"""
    try:
        # 获取请求数据
        if request.is_json and request.json is not None:
            data = request.json
        else:
            return jsonify({
                "status": "error",
                "message": "请求格式错误，请使用JSON格式"
            }), 400
        
        # 获取token参数
        token = data.get("token")
        if not token:
            return jsonify({
                "status": "error",
                "message": "缺少必需参数token"
            }), 400
        
        # 根据token获取用户信息
        from database.operations import get_user_by_token
        user = get_user_by_token(token)
        
        if not user:
            return jsonify({
                "status": "error",
                "message": "token无效或已过期"
            }), 401
        
        # 返回用户数据
        return jsonify({
            "status": "success",
            "message": "自动登录成功",
            "user": {
                "id": user.id,
                "point": user.point
            },
            "token": token
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"自动登录失败: {str(e)}"
        }), 500

@app.route("/auth/logout", methods=["POST"])
def logout():
    """退出登录"""
    try:
        return jsonify({"message": "退出登录成功"}), 200
    except Exception as e:
        return jsonify({"error": f"退出登录失败: {str(e)}"}), 500


if __name__ == "__main__":
    # 根据环境变量决定是否启用调试模式
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    port = int(os.environ.get("PORT", DEFAULT_PORT))

    app.run(debug=debug_mode, host="0.0.0.0", port=port)
