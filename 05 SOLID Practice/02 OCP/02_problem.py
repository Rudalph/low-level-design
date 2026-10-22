'''
Question 2: Employee Bonus Calculation System (Easy–Medium)

You are developing a system for a company that calculates employee bonuses based on their employee type.

The system should perform the following tasks:
    1. Store employee details (ID, name, employee type, and basic salary).
    2. Calculate bonuses based on employee type:
        - Full-Time Employee: 20% of basic salary
        - Part-Time Employee: 10% of basic salary
        - Contract Employee: 5% of basic salary
    3. Calculate the total salary:
        Total Salary = Basic Salary + Bonus
    4. Display the employee's details, bonus amount, and total salary.
    5. The company may introduce new employee types in the future, each having its own bonus calculation rules.

Your Task: Implement the Employee Bonus Calculation System using OOP while following OCP and SRP. 
Demonstrate that you can introduce an Intern Employee with a 3% bonus 
without modifying existing bonus calculation classes.
'''

from abc import ABC, abstractmethod

class EmployeeDetails:
    def __init__(self, id, name, employee_type, basic_salary):
        self.id = id
        self.name = name
        self.employee_type = employee_type
        self.basic_salary = basic_salary
        
    def get_basic_salary(self):
        return self.basic_salary

class CalculateBonus(ABC):
    @abstractmethod
    def bonus_calculator(self):
        pass
    
class CalculateFullTimeEmployeeBonus(CalculateBonus):
    def __init__(self, employee):
        self.employee = employee
    
    def bonus_calculator(self):
        return (self.employee.get_basic_salary() * 20) / 100

class CalculatePartTimeEmployeeBonus(CalculateBonus):
    def __init__(self, employee):
        self.employee = employee
    
    def bonus_calculator(self):
        return (self.employee.get_basic_salary() * 10) / 100

class CalculateContractEmployeeBonus(CalculateBonus):
    def __init__(self, employee):
        self.employee = employee
    
    def bonus_calculator(self):
        return (self.employee.get_basic_salary() * 5) / 100

class TotalSalaryCalculator:
    def __init__(self, employee, bonus_calculator):
        self.employee = employee
        self.bonus_calculator = bonus_calculator
    
    def total_salary(self):
        return self.employee.get_basic_salary() + self.bonus_calculator.bonus_calculator()
    
class SalaryPrinter:
    def __init__(self, employee, salary_calculator, bonus_calculator):
        self.employee = employee
        self.salary_calculator = salary_calculator
        self.bonus_calculator = bonus_calculator
        
    def print_salary(self):
        print(f'Employee Name: {self.employee.name}')
        print(f'Employee Id: {self.employee.id}')
        print(f'Employee Type: {self.employee.employee_type}')
        print(f'Basic Salary: {self.employee.get_basic_salary()}')
        print(f'Employee Bonus: {self.bonus_calculator.bonus_calculator()}')
        print(f'Employee Salary: {self.salary_calculator.total_salary()}')

'''In future we want to implement intern's 3% bonus'''
class CalculateInternEmployeeBonus(CalculateBonus):
    def __init__(self, employee):
        self.employee = employee

    def bonus_calculator(self):
        return self.employee.get_basic_salary() * 0.03

employee = EmployeeDetails(1, "Rudalph", 'Full Time', 40000)
bonus_calculator = CalculateFullTimeEmployeeBonus(employee)
salary_calculator = TotalSalaryCalculator(employee, bonus_calculator)
salary_printer = SalaryPrinter(employee, salary_calculator, bonus_calculator)
salary_printer.print_salary()