from datetime import timedelta, datetime

import jwt
from decouple import config


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=1)
        }
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")
