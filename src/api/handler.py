from src.api.authorizer import Authorizer
from src.api.normalizer import Normalizer
import json


def login_handler(event, _):
    body = json.loads(event["body"])
    return Authorizer().login(body["user"], body["password"])


def normalize_handler(event, _):
    Authorizer().verify_token(event["headers"]["token"])
    return Normalizer().normalize(json.loads(event["body"]))