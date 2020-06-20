from constants import Collections
from mymongo import Database
from models import Assignment, Classroom, Subject, Syllabus, Field
import pprint

from pymongo import MongoClient

###########################  Example one  ##############################
# db = Database("WD")
#
# col_name = Collections.STUDENT
#
# data = {"first_name": "Kevin",
#         "last_name": "Rodriguez",
#         "_id": "457845"
#         }
#
# inserted_id = db.insert(col_name, data)
# print('inserted_id: ', inserted_id)
#
# data = {"first_name": "Kevin",
#         "last_name": "Maj",
#         "_id": "457845"
#         }
#
# db.update_by_id(col_name, data, "457845")
#
# print(db.find_one(col_name, data))
#
# all = db.find_all(col_name, {"first_name": "Kevin"})
# for a in all:
#     print(a)
#
# found_one = db.find_by_id(col_name, "457845")
#
# print(found_one)


###########################  Example 2  ##############################

# a = Assignment()
# # a.id = "1"
# a.grade = "1"
# a.student_id = "1"
# a.subject_id = "1"
# a.add_student_grade()
#
# db = Database("WD")
# col, data = a.build_data()
# db.insert(col, data)

###########################  Example 3  ##############################

# db = Database("WD")
# data = db.find_by_id(Collections.ASSIGNMENT, "1")
# print("Data:", data)
#
# a = Assignment(data)
# print(a.student_grade)
# a.grade = "3"
# a.student_id = "123123"
# a.add_student_grade()
# db.update_by_id(*a.build_data(), a.id)
# # print(db.index_info(Collections.ASSIGNMENT))

###########################  Example 4  ##############################

# a = Classroom()
# a.id = "1"
# a.name = "room_100"
# a.headset_cnt = "14"
# a.pc_cnt = "14"
# a.seats_cnt = "24"
# a.white_board = "Yes"
# a.projector = "Yes"
#
# db = Database("WD")
# # col, data = a.build_data()
# db.insert(*a.build_data())
# # al = db.query(Collections.CLASSROOM, {"description": {"$elemMatch": {"projector": "Yes" ''', "white_board": "Yes" '''}}})
# al = db.query(Collections.CLASSROOM, {"description.projector": "Yes"})
# print(al)
# for a in al:
#     print(a)

###########################  Example 5  ##############################

# a = Subject()
# a.id = "23"
# a.name = "Math"
# a.field = "Informatyka Techniczna"
# a.ects = "6"
# a.exam = "Yes"
# a.lab_cnt = "30"
# a.lectures_cnt = "80"
# a.project = "Yes"
#
# db = Database("WD")
# # col, data = a.build_data()
# db.insert(*a.build_data())
# # al = db.query(Collections.CLASSROOM, {"description": {"$elemMatch": {"projector": "Yes" ''', "white_board": "Yes" '''}}})
# al = db.query(Collections.SUBJECT, {"details.ects": "6"})
# print(al)
# for a in al:
#     print(a)

###########################  Example 6  ##############################

# a = Syllabus()
# a.id = "1"
# a.faculty = "WIMiIP"
# a.field = "IT"
# a.description = "This is the syllabus of IT studies."
# a.year = 2018
# a.full_time_studies = "Yes"
# a.subject_id = "1"
#
#
# db = Database("WD")
# # col, data = a.build_data()
# db.insert(*a.build_data())
# a.subject_id = "2"
# db.update_by_id(*a.build_data(), a.id)
# a.subject_id = "34"
# db.update_by_id(*a.build_data(), a.id)
#
# # al = db.query(Collections.CLASSROOM, {"description": {"$elemMatch": {"projector": "Yes" ''', "white_board": "Yes" '''}}})
# al = db.query(Collections.SYLLABUS, {"subjects.subject_id": "34"})
# print(al)
# for a in al:
#     print(a)


###########################  Example 7  ##############################

# a = Field()
# a.id = "3"
# a.faculty = "WIMiIP"
# a.name = "Informatyka Techniczna"
# a.subject_id = "23"
#
# db = Database("WD")
# col, data = a.build_data()
# db.insert(*a.build_data())
# a.subject_id = "33"
# db.update_by_id(*a.build_data(), a.id)
# a.subject_id = "34"
# db.update_by_id(*a.build_data(), a.id)
#
# # al = db.query(Collections.CLASSROOM, {"description": {"$elemMatch": {"projector": "Yes" ''', "white_board": "Yes" '''}}})
# al = db.query(Collections.SYLLABUS, {"subjects.subject_id": "34"})
# print(al)
# for a in al:
#     print(a)

host = "db2020-aggregations-2sawx.mongodb.net"
login = "zabd2020"
password = "aggregations"

connection = Database.connect_net(host, login, password)

# col = connection["db-aggregations"]
# a = col["movies"].find_one({"year": 1893})
# print(a)

### ad 1 ###
# collection = connection["db-aggregations"]
# a = collection["movies"].aggregate([
#                                 {"$match": {"languages": {"$in": ["English", "German"]}, "imdb.rating": {"$gte": 0}}},
#                                 {"$project": {"_id": 0, "title": "$title", "rating": "$imdb.rating"}},
#                                 {"$sort": {"rating": -1}}
#                                 ])
# for i, x in enumerate(a):
#     pprint.pprint(x)


# # ### ad 2 ###
# collection = connection["db-aggregations"]
# a = collection["movies"].aggregate([
#                                 {"$match": {"year": {"$gt": 1960},
#                                             "imdb.rating": {"$gt": 5},
#                                             "directors": {"$exists": "true"},
#                                             "cast": {"$exists": "true"}}
#                                  },
#                                 {"$project": {"_id": 0,
#                                               "title": "$title",
#                                               "rating": "$imdb.rating",
#                                               "cast_dir": {"$setIsSubset": ["$cast", "$directors"]},
#                                               "cast": "$cast",
#                                               "directors": "$directors"}
#                                  },
#                                 {"$match": {"cast_dir": True}
#                                  },
#                                 {"$project": {"title": "$title",
#                                               "rating": "$rating"}
#                                  },
#                                 {'$count': "Director_actors"}
#                                 ])
# for i, x in enumerate(a):
#     pprint.pprint(x)

# ### ad 2 extension ###
# collection = connection["db-aggregations"]
# a = collection["movies"].aggregate([
#                                 {"$match": {"year": {"$gt": 1960},
#                                             "imdb.rating": {"$gt": 5},
#                                             "directors": {"$exists": "true"},
#                                             "cast": {"$exists": "true"}}
#                                  },
#                                 {"$project": {"_id": 0,
#                                               "title": "$title",
#                                               "rating": "$imdb.rating",
#                                               "cast_dir": {"$setIsSubset": ["$cast", "$directors"]},
#                                               "cast": "$cast",
#                                               "directors": "$directors"}
#                                  },
#                                 {"$match": {"cast_dir": True}
#                                  },
#                                 {"$project": {"title": "$title",
#                                               "rating": "$rating",
#                                               "directors": "$directors"}},
#                                 {"$group": {"_id": {"rating": "$rating"},
#                                             "dirs": {"$addToSet": "$directors"}},
#                                  },
#                                 {"$sort": {"_id.rating": -1}},
#                                 {"$limit": 10}
#
#                                 ])
#
# for i, x in enumerate(a):
#     pprint.pprint(x)
#     # if i == 3:
#     #     break

# ### ad 3 ###
# collection = connection["db-aggregations"]
# a = collection["movies"].aggregate([
#                                 {'$unwind': {'path': '$cast'}},
#                                 {'$group': {'_id': '$cast', 'aver': {'$avg': '$imdb.rating'}}},
#                                 {'$sort': {'aver': -1}},
#                                 {'$limit': 10}
#                                 ])
#
#
# for i, x in enumerate(a):
#     pprint.pprint(x)
#     # if i == 3:
#     #     break


#  ### ad 4 ###
# a = connection['db-aggregations']['air_alliances'].aggregate([
#     {'$unwind': {'path': '$airlines'}},
#     {'$lookup': {'from': 'air_routes', 'localField': 'airlines', 'foreignField': 'airline.name', 'as': 'routes'}},
#     {'$unwind': {'path': '$routes'}},
#     {'$match': {'routes.dst_airport': 'BCN'}},
#     {'$group': {'_id': '$name', 'routes_cnt': {'$sum': 1}}},
#     {'$sort': {'routes_cnt': -1}},
#     {'$limit': 1}
# ])
#
#
# for i, x in enumerate(a):
#     pprint.pprint(x)


# Wszystkie lotniska do ktorych można dotrzeć w max 2 przesiadkach
### ad 5 ###
a = connection['db-aggregations']['air_routes'].aggregate([
    {'$graphLookup': {
        'from': 'air_routes',
        'startWith': "$dst_airport",
        'connectFromField': "dst_airport",
        'connectToField': 'src_airport',
        'maxDepth': 1,
        'as': "destinations",
        'depthField': "stops_after"
    }},
    {'$match': {'src_airport': "BNC"}},
    {'$project': {'src_airport': '$src_airport', 'dst_airport': '$dst_airport', 'destinations': '$destinations'}},
    {'$unwind': {'path': '$destinations'}},
    {'$group': {
        '_id': {"src": '$src_airport'},
        "dst_max_2": {"$addToSet": "$destinations.dst_airport"}}}

]
)

for i, x in enumerate(a):
    pprint.pprint(x)
    if i == 3:
        break
