import bcrypt

def hash_password(password: str) -> str:
    """
    Hashear uma senha em texto puro usando bcrypt.
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verificar se a senha em texto puro corresponde ao hash armazenado.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
