from constants import Collections
from mymongo import Database
from models import Assignment
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
# a.id = "1"
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


