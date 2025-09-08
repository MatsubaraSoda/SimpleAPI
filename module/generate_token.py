import secrets

def generate_token():
    """生成一个安全的随机 token"""
    return secrets.token_hex(16)