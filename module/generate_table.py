from faker import Faker
import random

# =============================================================================
# 配置常量
# =============================================================================
MAX_ROWS = 32

# =============================================================================
# 全局变量
# =============================================================================
# 全局 Faker 实例
fake = Faker('zh_CN')

# 全局唯一性跟踪器
phone_tracker = set()

# =============================================================================
# 数据生成函数
# =============================================================================
def generate_id(row_index):
    """
    生成自增ID
    
    Args:
        row_index (int): 行索引（从0开始）
        
    Returns:
        int: 自增ID（从1开始）
    """
    return row_index + 1


def generate_name():
    """
    生成随机中文姓名
    
    Returns:
        str: 随机中文姓名
    """
    return fake.name()


def generate_phone():
    """
    生成唯一手机号
    
    Returns:
        str: 唯一的手机号（纯数字格式）
    """
    max_attempts = 1000
    
    for _ in range(max_attempts):
        phone = fake.phone_number()
        # 清理格式，只保留数字
        phone = ''.join(filter(str.isdigit, phone))
        
        if phone not in phone_tracker:
            phone_tracker.add(phone)
            return phone
    
    # 如果无法生成唯一手机号，返回空字符串
    return ""


def generate_row(row_index):
    """
    生成单行数据（固定三个字段：id, name, phone）
    
    Args:
        row_index (int): 行索引（从0开始）
        
    Returns:
        dict: 包含id、name、phone的字典
    """
    return {
        'id': generate_id(row_index),
        'name': generate_name(),
        'phone': generate_phone()
    }


def generate_table_data(rows):
    """
    生成表格数据主函数
    
    Args:
        rows (int): 要生成的行数（1-32）
        
    Returns:
        list: 包含多行数据的列表
    """
    result = []
    
    for i in range(rows):
        row_data = generate_row(i)
        result.append(row_data)
    
    return result


