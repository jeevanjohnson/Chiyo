import config
from pymongo import MongoClient
from pymongo.collection import Collection

class Mongo:
    def __init__(
        self, 
        connection_access: str = config.connection_access, 
        path: list[str] = config.db_path
    ) -> None:
        self._db = db = MongoClient(connection_access)
        
        for p in path:
            db = db[p]

        self.users: Collection = db['users']
        self.prefixes: Collection = db['prefixes']