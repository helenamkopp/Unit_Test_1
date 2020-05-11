import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("Helena", "Kopp", 7500)
        self.emp_2 = Employee("Romulo", "Rosa", 9800)

    def tearDown(self):
        pass

    def test_email(self):

        self.assertEqual(self.emp_1.email, "Helena.Kopp@email.com")
        self.assertEqual(self.emp_2.email, "Romulo.Rosa@email.com")

        self.emp_1.first = "Isabela"
        self.emp_2.first = "Jose"

        self.assertEqual(self.emp_1.email, "Isabela.Kopp@email.com")
        self.assertEqual(self.emp_2.email, "Jose.Rosa@email.com")

        self.emp_1.last = "Kondo"
        self.emp_2.last = "Silva"

        self.assertEqual(self.emp_1.email, "Isabela.Kondo@email.com")
        self.assertEqual(self.emp_2.email, "Jose.Silva@email.com")


    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Helena Kopp")
        self.assertEqual(self.emp_2.fullname, "Romulo Rosa")

        self.emp_1.first = "Isabela"
        self.emp_2.first = "Jose"

        self.assertEqual(self.emp_1.fullname, "Isabela Kopp")
        self.assertEqual(self.emp_2.fullname, "Jose Rosa")


    def test_apllyraise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 7875)
        self.assertEqual(self.emp_2.pay, 10290)

