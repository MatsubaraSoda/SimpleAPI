import re

# 配置常量
MAX_EXPRESSION_LENGTH = 32


def validate_arithmetic_expression(expression):
    """
    验证四则运算表达式的合法性（简化版本）
    只检查基本字符和长度，避免恶意注入
    
    Args:
        expression (str): 要验证的表达式
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not expression:
        return False, "表达式不能为空"
    
    # 检查长度
    if len(expression) > MAX_EXPRESSION_LENGTH:
        return False, f"表达式长度不能超过 {MAX_EXPRESSION_LENGTH} 个字符"
    
    # 检查字符合法性：只允许数字、小数点、四则运算符号、圆括号、空格
    valid_pattern = r"^[\d\.\+\-\*\/\(\)\s]+$"
    if not re.match(valid_pattern, expression):
        return False, "表达式包含非法字符，只允许数字、小数点、四则运算符号(+、-、*、/)、圆括号和空格"
    
    return True, ""
