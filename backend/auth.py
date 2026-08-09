import bcrypt


def hash_password(password: str) ->str:
    bpwd = password.encode()
    salt = bcrypt.gensalt()
    hashpwd = bcrypt.hashpw(bpwd, salt)
    return hashpwd.decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    b_plain_pwd = plain_password.encode()
    b_hashed_pwd = hashed_password.encode()
    is_pwd = bcrypt.checkpw(b_plain_pwd, b_hashed_pwd)
    return is_pwd
