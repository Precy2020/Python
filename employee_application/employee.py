from employee_application.employee_exception import EmployeeException


class Employee:
    __emp_id = 0

    def __init__(self, emp_name: str, emp_department: str):
        self.__emp_id += 1
        self.__emp_name = emp_name
        self.__emp_department = emp_department
        self.__hourly_rate = 10
        self.__number_of_hours_worked = 0

    def get_emp_id(self):
        return self.__emp_id

    def calculate_emp_salary(self, numbers_of_hours_worked):
        if numbers_of_hours_worked > 0:
            numbers_of_hours_worked *= self.__hourly_rate
            self.__number_of_hours_worked = numbers_of_hours_worked
        else:
            raise EmployeeException("This input is not valid")

    def get_salary(self):
        return self.__number_of_hours_worked

    def emp_assign_department(self, emp_department: str):
        return self.__emp_department == emp_department

    def print_employee_details(self, emp_department, emp_id: int, emp_name: str):
        return self.emp_assign_department(
            emp_department) and self.get_emp_id() == emp_id and self.__emp_name == emp_name
