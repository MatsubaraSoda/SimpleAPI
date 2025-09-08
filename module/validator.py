import re

# =============================================================================
# 配置常量
# =============================================================================
MAX_EXPRESSION_LENGTH = 32
MAX_ROWS = 32

# 表格生成API固定返回字段（无需验证，因为固定返回）
FIXED_FIELDS = ["id", "name", "phone"]


# =============================================================================
# 算术表达式验证函数
# =============================================================================
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


# =============================================================================
# 表格生成API验证函数
# =============================================================================
def validate_table_request(data):
    """
    表格生成API参数验证主函数
    
    Args:
        data (dict): 请求数据
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    # 注意：JSON格式验证在 app.py 中使用 request.is_json 处理
    
    # 1. 必要参数检查
    if not _check_required_params(data):
        return False, "缺少必要参数"
    
    # 2. rows参数验证
    if not _validate_rows(data.get('rows')):
        return False, "数据量错误，rows参数应在1-32之间"
    
    return True, ""


def _check_required_params(data):
    """
    检查必要参数是否存在（内部函数）
    
    Args:
        data (dict): 请求数据
        
    Returns:
        bool: 是否包含必要参数
    """
    return (
        isinstance(data, dict) and
        'rows' in data
    )


def _validate_rows(rows):
    """
    验证rows参数（内部函数）
    
    Args:
        rows: 行数参数
        
    Returns:
        bool: 是否有效
    """
    return (
        isinstance(rows, int) and 
        1 <= rows <= MAX_ROWS
    )

