import bcrypt
from argon2 import PasswordHasher

def password_hash(password):
    # bcrypt
    bcrypt_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # argon2
    ph = PasswordHasher()
    argon2_hash = ph.hash(password)

    return bcrypt_hash, argon2_hash