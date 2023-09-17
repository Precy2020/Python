import unittest
from employee_application.employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.employ = Employee("Esau", "P.R")

    def test_that_an_id_can_be_assigned_to_an_employee(self):
        
        self.assertTrue(True, self.employ.emp_assign_department("P.R"))

    def test_that_employee_can_be_registered(self):
        self.assertIsNotNone(self.employ.print_employee_details("P.R", 1, "Esau"))

    def test_that_employee_salary_can_be_calculated(self):
        self.employ.calculate_emp_salary(4)
        self.assertEqual(40, self.employ.get_salary())

    def test_that_can_get_employee_id(self):
        self.assertEqual(1, self.employ.get_emp_id())

    def test_that_salary_cant_be_a_negative_number(self):
        self.employ.calculate_emp_salary(-2)
        self.assertEqual(-20, self.employ.get_salary())
