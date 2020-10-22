import json

class User:

    def __init__(self, username):
        self.inventory = []
        self.username = username

    def jsonformat(self):
        # jsonobj = {}
        # for prop in dir(self):
        #     jsonobj[prop] = dir(self)[prop]
        return json.dumps(dir(self))
    