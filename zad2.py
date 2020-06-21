from constants import Collections
from mymongo import Database
from models import Assignment, Classroom, Subject, Syllabus, Field
import pprint
import json

host = "db2020-aggregations-2sawx.mongodb.net"
login = "zabd2020"
password = "aggregations"

connection = Database.connect_net(host, login, password)

# ### ad 1 ###
# print("Zadanie 1")
# a = connection["db-aggregations"]["movies"].aggregate([
#     {"$match": {"languages": {"$in": ["English", "German"]},
#                 "imdb.rating": {"$gte": 0}}},
#     {"$project": {"_id": 0, "title": "$title", "rating": "$imdb.rating"}},
#     {"$sort": {"rating": -1}}
# ])
# print("Show first 10 values:")
# for i, x in enumerate(a):
#     pprint.pprint(x)
#     if i == 9:
#         break
#
#
# # ### ad 2 ###
# print()
# print()
# print("Zadanie 2")
# a = connection["db-aggregations"]["movies"].aggregate([
#     {"$match": {"year": {"$gt": 1960},
#                 "imdb.rating": {"$gt": 5},
#                 "directors": {"$exists": "true"},
#                 "cast": {"$exists": "true"}}},
#     {"$project": {"_id": 0,
#                   "title": "$title",
#                   "rating": "$imdb.rating",
#                   "cast_dir": {"$setIsSubset": ["$cast", "$directors"]},
#                   "cast": "$cast",
#                   "directors": "$directors"}},
#     {"$match": {"cast_dir": True}},
#     {"$project": {"title": "$title",
#                   "rating": "$rating"}},
#     {'$count': "Director_actors"}
# ])
#
# for i, x in enumerate(a):
#     pprint.pprint(x)
#
# # ### ad 2 extended ###
# # collection = connection["db-aggregations"]
# # a = collection["movies"].aggregate([
# #                                 {"$match": {"year": {"$gt": 1960},
# #                                             "imdb.rating": {"$gt": 5},
# #                                             "directors": {"$exists": "true"},
# #                                             "cast": {"$exists": "true"}}
# #                                  },
# #                                 {"$project": {"_id": 0,
# #                                               "title": "$title",
# #                                               "rating": "$imdb.rating",
# #                                               "cast_dir": {"$setIsSubset": ["$cast", "$directors"]},
# #                                               "cast": "$cast",
# #                                               "directors": "$directors"}
# #                                  },
# #                                 {"$match": {"cast_dir": True}
# #                                  },
# #                                 {"$project": {"title": "$title",
# #                                               "rating": "$rating",
# #                                               "directors": "$directors"}},
# #                                 {"$group": {"_id": {"rating": "$rating"},
# #                                             "dirs": {"$addToSet": "$directors"}},
# #                                  },
# #                                 {"$sort": {"_id.rating": -1}},
# #                                 {"$limit": 10}
# #
# #                                 ])
# #
# # for i, x in enumerate(a):
# #     pprint.pprint(x)
# #     # if i == 3:
# #     #     break
#
# ### ad 3 ###
# print()
# print()
# print("Zadanie 3")
# a = connection["db-aggregations"]["movies"].aggregate([
#     {'$unwind': {'path': '$cast'}},
#     {'$group': {'_id': '$cast', 'aver': {'$avg': '$imdb.rating'}}},
#     {'$sort': {'aver': -1}},
#     {'$limit': 10}
# ])
#
# for i, x in enumerate(a):
#     pprint.pprint(x)
#
#
# ### ad 4 ###
# print()
# print()
# print("Zadanie 4")
# a = connection['db-aggregations']['air_alliances'].aggregate([
#     {'$unwind': {'path': '$airlines'}},
#     {'$lookup': {'from': 'air_routes',
#                  'localField': 'airlines',
#                  'foreignField': 'airline.name',
#                  'as': 'routes'}},
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
#
#
# # Wszystkie lotniska do ktorych można dotrzeć w max 2 przesiadkach
# ### ad 5a ###
# print()
# print()
# print("Zadanie 5a")
# a = connection['db-aggregations']['air_routes'].aggregate([
#     {'$graphLookup': {
#         'from': 'air_routes',
#         'startWith': "$dst_airport",
#         'connectFromField': "dst_airport",
#         'connectToField': 'src_airport',
#         'maxDepth': 2,
#         'as': "destinations",
#         'depthField': "stops_after"
#     }},
#     {'$match': {'src_airport': "BNC"}},
#     {'$unwind': {'path': '$destinations'}},
#     {'$group': {
#         '_id': {"src": '$src_airport'},
#         "dst_max_2": {"$addToSet": "$destinations.dst_airport"}}}
# ])
#
# for i, x in enumerate(a):
#     pprint.pprint(x)

### ad 9 ###
print("Zadanie 9")
a = connection["db-aggregations"]["movies"].aggregate([
    {'$facet': {
        'categorizedByYears(Auto)': [
            {'$bucketAuto': {
                'groupBy': '$year',
                'buckets': 50,
            }}
        ],
        'categorizedByRating': [
            {'$bucket': {
                'groupBy': "$imdb.rating",
                'boundaries': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'default': "Other",
                'output': {
                    "count": {'$sum': 1},
                    'titles': {'$push': '$title'}
                     }
                }}
             ]
        }
     }

])
print("Show first 10 values:")
for i, x in enumerate(a):
    pprint.pprint(x)

    if i == 9:
        break