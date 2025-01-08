from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from infra.sqlalchemy.user.AlchemyUserRepo import AlchemyUserRepo
from repos.user.IUserRepo import IUserRepo
from schemas.pydantic.auth.login.TokenData import TokenData
from configs.Environment import get_env
from schemas.pydantic.auth.Token import Token

env = get_env()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


async def get_current_user(
    token=Depends(oauth2_scheme), user_repo: IUserRepo = Depends(AlchemyUserRepo)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, env.JWT_SECRET_KEY, algorithms=[env.JWT_ALGORITHM])
        email = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except JWTError:
        raise credentials_exception

    user = await user_repo.load_active_first(email=token_data.username)
    if user is None:
        raise credentials_exception
    return user
