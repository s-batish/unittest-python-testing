# import unittest
# from student import Student


# class TestStudent(unittest.TestCase):
#     def test_full_name(self):
#         student = Student("John", "Doe")
#         self.assertEqual(student.full_name, "John Doe")

#     def test_alert_santa(self):
#         student = Student("John",  "Doe")
#         student.alert_santa()
#         self.assertTrue(student.naughty_list)

#     def test_email(self):
#         student = Student("John", "Doe")
#         self.assertEqual(student.email, "john.doe@email.com")


# if __name__ == "__main__":
#     unittest.main()

import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")


if __name__ == "__main__":
    unittest.main()
