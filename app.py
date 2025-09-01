from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    """首页路由"""
    return jsonify({
        "message": "SimpleAPI - 无数据库依赖的实时计算API服务",
        "version": "1.0.0",
        "apis": [
            {
                "endpoint": "/calculate",
                "method": "GET/POST",
                "description": "计算算术表达式",
                "example": "/calculate?expression=2+3*4"
            }
        ]
    })

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    """计算表达式API"""
    try:
        # 获取表达式参数
        if request.method == 'GET':
            expression = request.args.get('expression', '')
        else:
            expression = request.json.get('expression', '') if request.is_json else request.form.get('expression', '')
        
        if not expression:
            return jsonify({"error": "缺少表达式参数", "usage": "请提供expression参数"}), 400
        
        # 安全校验
        if not is_safe_expression(expression):
            return jsonify({"error": "表达式包含不安全字符", "usage": "仅支持数字、运算符和括号"}), 400
        
        # 计算结果
        result = evaluate_expression(expression)
        
        return jsonify({
            "expression": expression,
            "result": result,
            "status": "success"
        })
        
    except Exception as e:
        return jsonify({"error": f"计算失败: {str(e)}"}), 500

def is_safe_expression(expression):
    """检查表达式是否安全"""
    # 只允许数字、运算符、括号和空格
    safe_pattern = r'^[\d\+\-\*\/\(\)\s\.]+$'
    return bool(re.match(safe_pattern, expression))

def evaluate_expression(expression):
    """计算表达式（简化版本）"""
    try:
        # 移除所有空格
        expression = expression.replace(' ', '')
        
        # 使用Python的eval函数（在安全校验后使用）
        # 注意：这里假设is_safe_expression已经过滤了危险字符
        result = eval(expression)
        
        # 处理除零错误
        if isinstance(result, (int, float)):
            return result
        else:
            raise ValueError("计算结果类型错误")
            
    except ZeroDivisionError:
        raise ValueError("除零错误")
    except Exception as e:
        raise ValueError(f"表达式计算失败: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
