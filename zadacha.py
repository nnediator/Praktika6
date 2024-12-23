import peewee as pw

db = pw.SqliteDatabase('sqlite_python.db')

class BaseModel(pw.Model):
    class Meta:
        database = db

class Student(BaseModel):
    students_id = pw.IntegerField(primary_key=True)
    students_name = pw.CharField()
    students_surname = pw.CharField()
    students_age = pw.IntegerField()
    students_city = pw.CharField()

class Course(BaseModel):
    courses_id = pw.IntegerField(primary_key=True)
    courses_name = pw.CharField()
    courses_time_start = pw.DateField()
    courses_time_end = pw.DateField()

class StudentCourse(BaseModel):
    student = pw.ForeignKeyField(Student, backref='courses')
    course = pw.ForeignKeyField(Course, backref='students')

db.connect()
db.create_tables([Student, Course, StudentCourse])

def insert_students():
    students_data = [
        (1, 'Max', 'Brooks', 24, 'Spb'),
        (2, 'John', 'Stones', 15, 'Spb'),
        (3, 'Andy', 'Wings', 45, 'Manchester'),
        (4, 'Kate', 'Brooks', 34, 'Spb')
    ]
    with db.atomic():
        for student in students_data:
            Student.create(
                students_id=student[0],
                students_name=student[1],
                students_surname=student[2],
                students_age=student[3],
                students_city=student[4]
            )

def insert_courses():
    courses_data = [
        (1, 'python', '2021-07-21', '2021-08-21'),
        (2, 'java', '2021-07-13', '2021-08-16')
    ]
    with db.atomic():
        for course in courses_data:
            Course.create(
                courses_id=course[0],
                courses_name=course[1],
                courses_time_start=course[2],
                courses_time_end=course[3]
            )

def insert_student_courses():
    student_courses_data = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2)
    ]
    with db.atomic():
        for student_id, course_id in student_courses_data:
            StudentCourse.create(student=student_id, course=course_id)

def get_students_over_30():
    return Student.select().where(Student.students_age > 30)

def get_students_in_python():
    return Student.select().join(StudentCourse).where(StudentCourse.course == 1)

def get_students_in_python_from_spb():
    return Student.select().join(StudentCourse).where(
        (StudentCourse.course == 1) & (Student.students_city == 'Spb')
    )

insert_students()
insert_courses()
insert_student_courses()

if __name__ == '__main__':
    print("Студенты старше 30 лет:")
    for student in get_students_over_30():
        print(student.students_name, student.students_age)

    print("\nСтуденты, которые проходят курс по питону:")
    for student in get_students_in_python():
        print(student.students_name)

    print("\nСтуденты, которые проходят курс по питону и из Spb:")
    for student in get_students_in_python_from_spb():
        print(student.students_name)

db.close()