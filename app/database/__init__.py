import pymongo

class MongoDBConnection:
    def __init__(self, host='localhost', port=32768):
        self.host = host
        self.port = port
        self.client = None
        self.database = None

    def __enter__(self):
        self.client = pymongo.MongoClient(self.host, self.port)
        self.database = self.client['product_db']
        return self.database

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
