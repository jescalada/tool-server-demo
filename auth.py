from jose import jwt
from jose.exceptions import JWTError
import requests
from fastapi import HTTPException, status, Depends, Header

OIDC_CLIENT_ID = "1009968223893-u92qq6itk7ej5008o4174gjubs5lhorg.apps.googleusercontent.com"
OIDC_ISSUER = "https://accounts.google.com"
JWKS_URL = "https://www.googleapis.com/oauth2/v3/certs"

jwks_cache = {}

def get_jwk(kid: str):
    global jwks_cache
    if not jwks_cache:
        resp = requests.get(JWKS_URL)
        resp.raise_for_status()
        jwks = resp.json()
        if "keys" not in jwks:
            raise HTTPException(status_code=401, detail="Invalid JWKS: no keys found")
        keys = jwks["keys"]
        jwks_cache = {k["kid"]: k for k in keys}
    return jwks_cache.get(kid)

def verify_jwt(authorization: str = Header(...), access_token: str = Header(default=None, alias="X-Access-Token")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    token = authorization[len("Bearer "):]
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")
    jwk = get_jwk(kid)

    if not jwk:
        raise HTTPException(status_code=401, detail="Invalid token: unknown key")

    try:
        payload = jwt.decode(
            token,
            jwk,
            algorithms=["RS256"],
            audience=OIDC_CLIENT_ID,
            issuer=OIDC_ISSUER,
            access_token=access_token
        )
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"JWT validation failed: {e}")
