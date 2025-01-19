from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt import decode_access_token

auth_scheme = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        payload = decode_access_token(credentials.credentials)
        return payload["user_id"]
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")
