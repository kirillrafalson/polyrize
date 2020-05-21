import jwt
import hashlib
from datetime import datetime, timedelta


class UnauthorizedException(Exception):
    def __init__(self):
        super().__init__()


class Authorizer:
    def __init__(self):
        self._secret = 'secret'
        self._users = {
            'user1': 'password1',
            'user2': 'password2'
        }

    def login(self, user, password):
        if self._users.get(user, None) == password:
            hash_user_name = hashlib.md5(user.encode())
            token = jwt.encode(
                {
                    'user': hash_user_name.hexdigest(),
                    'exp': datetime.utcnow() + timedelta(minutes=5)
                },
                self._secret, algorithm='HS256')
            return token
        raise UnauthorizedException()

    def verify_token(self, token):
        decoded = jwt.decode(token, self._secret, algorithms='HS256')
        if decoded['user'] not in list(map(lambda k: self._hash_string(k), self._users.keys())):
            raise UnauthorizedException()

    def _hash_string(self, string):
        return hashlib.md5(string.encode()).hexdigest()
