import unittest

class TestDatabaseFunctions(unittest.TestCase):

    def setUpClass(cls):
        db.connect()
        db.create_tables([Student, Course, StudentCourse])
        insert_students()
        insert_courses()
        insert_student_courses()

    @classmethod
    def tearDownClass(cls):
        db.drop_tables([StudentCourse, Course, Student])
        db.close()

    def test_get_students_over_30(self):
        result = get_students_over_30()
        self.assertEqual(len(result), 2) 

    def test_get_students_in_python(self):
        result = get_students_in_python()
        self.assertEqual(len(result), 3) 

    def test_get_students_in_python_from_spb(self):
        result = get_students_in_python_from_spb()
        self.assertEqual(len(result), 1)  

if __name__ == '__main__':
    unittest.main()