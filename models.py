from constants import Collections

ACTUAL_VERSION = "3"


class Student:
    def __init__(self, data=None):
        self.id = data.get("_id")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")

    def build_data(self):
        data = {"_id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "schema_version": ACTUAL_VERSION
                }
        return Collections.STUDENT, data


class Employee:
    def __init__(self, data=None):
        self.id = data.get("_id")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")

    def build_data(self):
        data = {"_id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "schema_version": ACTUAL_VERSION
                }
        return Collections.EMPLOYEE, data


class Assignment:
    def __init__(self, data=None):
        if data is not None:
            self.id = data.get("_id")
            self.subject_id = data.get("subject_id")
            self.student_grade = data.get("student_grade")[0]
        else:
            self.id = None
            self.subject_id = None
            self.student_grade = list()
        self.student_id = None
        self.grade = None

    def build_data(self):
        data = {"_id": self.id,
                "subject_id": self.subject_id,
                "student_grade": [
                    self.student_grade
                ],

                "schema_version": ACTUAL_VERSION
                }
        return Collections.ASSIGNMENT, data

    def add_student_grade(self):
        if self.student_id and self.grade:
            student_grade = {
                "student_id": self.student_id,
                "grade": self.grade
            }
            self.student_grade.append(student_grade)
        else:
            print("Not defined: student_id, grade")


class Classroom:
    def __init__(self, data=None):
        if data is not None:
            self.id = data.get("_id")
            self.name = data.get("name")
            self.description = data.get("description")
            self.pc_cnt = self.description[0].get("pc_cnt")
            self.white_board = self.description[0].get("white_board")
            self.headset_cnt = self.description[0].get("headset_cnt")
            self.projector = self.description[0].get("projector")
            self.seats_cnt = self.description[0].get("seats_cnt")
        else:
            self.id = None
            self.name = None
            self.description = list()
            self.pc_cnt = None
            self.white_board = None
            self.headset_cnt = None
            self.projector = None
            self.seats_cnt = None

    def build_data(self):
        if self.pc_cnt and self.white_board and self.headset_cnt and self.projector and self.seats_cnt:
            data = {
                    "pc_cnt": self.pc_cnt,
                    "white_board": self.white_board,
                    "headset_cnt": self.headset_cnt,
                    "projector": self.projector,
                    "seats_cnt": self.seats_cnt
                }
            self.description.append(data)

        data = {"_id": self.id,
                "name": self.name,
                "description": self.description,
                "schema_version": ACTUAL_VERSION
                }
        return Collections.CLASSROOM, data


class Subject:
    def __init__(self, data=None):
        if data is not None:
            self.id = data.get("_id")
            self.name = data.get("name")
            self.field = data.get("field")
            self.employee_id = data.get("employee_id")
            self.details = self.details.get("details")
            self.ects = self.details[0].get("ects")
            self.exam = self.details[0].get("exam")
            self.lab_cnt = self.details[0].get("lab_cnt")
            self.lectures_cnt = self.details[0].get("lectures_cnt")
            self.project = self.details[0].get("project")
        else:
            self.id = None
            self.name = None
            self.field = None
            self.employee_id = None
            self.ects = None
            self.exam = None
            self.lab_cnt = None
            self.lectures_cnt = None
            self.project = None

    def build_data(self):
        data = {"_id": self.id,
                "name": self.name,
                "field": self.field,
                "details": {
                    "ects": self.ects,
                    "exam": self.exam,
                    "lab_cnt": self.lab_cnt,
                    "lectures_cnt": self.lectures_cnt,
                    "project": self.project
                },
                "schema_version": ACTUAL_VERSION
                }
        return Collections.SUBJECT, data


class Syllabus:
    def __init__(self, data=None):
        if data is not None:
            self.id = data.get("_id")
            self.faculty = data.get("faculty")
            self.field = data.get("field")
            self.description = data.get("description")
            self.year = data.get("year")
            self.full_time_studies = data.get("full_time_studies")
            self.subjects = data.get("subjects")
            self.subject_id = None
        else:
            self.id = None
            self.faculty = None
            self.field = None
            self.description = None
            self.year = None
            self.full_time_studies = None
            self.subjects = list()
            self.subject_id = None

    def build_data(self):
        if self.subject_id is not None:
            data = {
                "subject_id": self.subject_id
            }
            self.subjects.append(data)
        data = {"_id": self.id,
                "faculty": self.faculty,
                "field": self.field,
                "description": self.description,
                "year": self.year,
                "full_time_studies": self.full_time_studies,
                "subjects": self.subjects,
                "schema_version": ACTUAL_VERSION
                }
        return Collections.SYLLABUS, data


class Field:
    def __init__(self, data=None):
        if data is not None:
            self.id = data.get("_id")
            self.faculty = data.get("faculty")
            self.name = data.get("name")
            self.subjects = data.get("subjects")
            self.subject_id = None
        else:
            self.id = None
            self.faculty = None
            self.name = None
            self.subjects = list()
            self.subject_id = None

    def build_data(self):
        if self.subject_id is not None:
            data = {
                "subject_id": self.subject_id
            }
            self.subjects.append(data)
        data = {"_id": self.id,
                "name": self.name,
                "faculty": self.faculty,
                "subjects": self.subjects,
                "disciplines": [
                    "informatyka techniczna i telekomunikacja",
                    "inżynieria materiałowa"
                ],
                "schema_version": ACTUAL_VERSION
                }
        return Collections.FIELD, data

