from jwt import encode, decode
from os import getenv
from flask import jsonify
from datetime import datetime, timezone, timedelta

def write_token(data:dict):

    token = encode(payload={**data, 'exp': datetime.now(tz=timezone.utc) + timedelta(days=1)}, key=getenv('SECRET'), algorithm='HS256')

    return token.encode('UTF-8')