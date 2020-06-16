from pymongo import MongoClient


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    @staticmethod
    def connect():
        return MongoClient(host='localhost', port=27017)

    @staticmethod
    def connect_net(host, username, password):
        return MongoClient(host='mongodb+srv://'+host, username=username, password=password)

    def insert(self, collection, data):
        with self.connect() as db:
            try:
                inserted_id = db[self.db_name][collection].insert_one(data).inserted_id
                return inserted_id
            except:
                print("Entry with id {} already exists".format(data.get("_id")))
                return None

    def update_by_id(self, collection, data, id):
        with self.connect() as db:
            return db[self.db_name][collection].update_one({"_id": id}, {"$set": data})

    def find_one(self, collection, data):
        with self.connect() as db:
            return db[self.db_name][collection].find_one(data)

    def find_all(self, collection, data):
        with self.connect() as db:
            all = db[self.db_name][collection].find(data)
            return all

    def find_by_id(self, collection, id):
        with self.connect() as db:
            return db[self.db_name][collection].find_one({"_id": id})

    def delete(self, collection, data):
        with self.connect() as db:
            db[self.db_name][collection].delete_one(data)

    def delete_by_id(self, collection, id):
        with self.connect() as db:
            db[self.db_name][collection].delete_one({"_id": id})

    def index_info(self, collection):
        with self.connect() as db:
            return db[self.db_name][collection].index_information()

    # def find_key_value(self, collection, id):

    def query_field_value(self, collection, query, value):
        with self.connect() as db:
            return db[self.db_name][collection].find({query: {"$lte": value}})

    def query(self, collection, query):
        with self.connect() as db:
            print(query)
            return db[self.db_name][collection].find(query)

    def new_index(self):
        pass

#
# a = Database("WD")
# a = a.query_field_value("Assignment", "student_grade.0.grade", "3")
# print(a)
#
# for x in a:
#     print(x)

