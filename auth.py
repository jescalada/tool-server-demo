import requests
from fastapi import HTTPException, status, Depends, Header
import os

USER_INFO_URL = os.getenv("USER_INFO_URL", "https://openidconnect.googleapis.com/v1/userinfo")

def verify_jwt(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    token = authorization[len("Bearer "):]
    print('DEBUG: token', token)

    resp = requests.get(
        USER_INFO_URL,
        headers={"Authorization": f"Bearer {token}"}
    )
    if resp.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid access token")
    print('DEBUG: resp', resp.json())
    return resp.json()
