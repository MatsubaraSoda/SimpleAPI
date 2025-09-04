from flask import Flask, request, jsonify
import os
from module.validator import validate_arithmetic_expression
from module.calculator import calculate_expression

app = Flask(__name__)

# 配置常量
API_VERSION = "1.0.0"
DEFAULT_PORT = 5000


@app.route("/")
def home():
    """首页路由"""
    return jsonify(
        {
            "message": "SimpleAPI - 无数据库依赖的实时计算API服务",
            "version": API_VERSION,
            "apis": [
                {
                    "endpoint": "/calculate",
                    "method": "POST",
                    "description": "计算算术表达式",
                    "example": 'POST /calculate with JSON: {"expression": "2+3*4"}',
                }
            ],
        }
    )


@app.route("/calculate", methods=["POST"])
def calculate():
    """计算表达式API"""
    try:
        # 获取表达式参数
        expression = (
            request.json.get("expression", "")
            if request.is_json
            else request.form.get("expression", "")
        )

        # 验证输入
        is_valid, error_message = validate_arithmetic_expression(expression)
        if not is_valid:
            return jsonify({"expression": expression, "error": error_message}), 400

        # 计算表达式
        result, status_code = calculate_expression(expression)
        return jsonify(result), status_code

    except Exception as e:
        return jsonify({"error": f"请求处理失败: {str(e)}"}), 500


if __name__ == "__main__":
    # 根据环境变量决定是否启用调试模式
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    port = int(os.environ.get("PORT", DEFAULT_PORT))

    app.run(debug=debug_mode, host="0.0.0.0", port=port)
