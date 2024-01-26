from model.user import User
import json


class Post:

    def __init__(self, body: str, author: User, id: int):
        self.body = body
        self.author = author
        self.id = id

