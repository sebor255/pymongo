from constants import Collections

ACTUAL_VERSION = "2"


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
        student_grade = {
                        "student_id": self.student_id,
                        "grade": self.grade
                    }
        self.student_grade.append(student_grade)


class Classroom:
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
        return Collections.CLASSROOM, data


# STUDENT = 'Student'
# EMPLOYEE = 'Employee'
# ASSIGNMENT = 'Assignment'
# CLASSROOM = 'Classroom'
# CLASSES = 'Classes'
# SUBJECT = 'Subject'
# STUDENT_GROUP = 'Student_group'
# SUBJECT_GROUP = 'Subject_group'


