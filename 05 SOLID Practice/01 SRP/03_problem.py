'''
You are developing a payroll system for a company that manages employee salaries.

The system should perform the following tasks:
    1. Store employee details (ID, name, department, and basic salary).
    2. Calculate the gross salary using:
        - HRA = 20% of basic salary.
        - DA = 10% of basic salary.
        - Gross Salary = Basic Salary + HRA + DA.
    3. Calculate deductions:
        - Tax = 10% of gross salary.
        - Provident Fund (PF) = 5% of basic salary.
    4. Calculate the net salary after deductions.
    5. Generate a payslip showing employee details, earnings, deductions, and net salary.
    6. Save the payslip to a .txt file.
    7. Send a salary notification (simulate this by printing a message to the console).

Your Task: Implement the payroll system using OOP while ensuring that each class follows the Single Responsibility Principle.
'''

class EmployeeDetails:
    def __init__(self, id, name, department, basic_salary):
        self.employee_id = id
        self.employee_name = name
        self.employee_department = department
        self.employee_basic_salary = basic_salary
        
    def get_employee_details(self):
        return {
            'id' : self.employee_id,
            'name' : self.employee_name,
            'department' : self.employee_department,
            'basic_salary' : self.employee_basic_salary
        }
        
class GrossSalaryCalculator:
    def __init__(self, employee):
        self.employee = employee
        self.hra = 0
        self.da = 0
        self.gross_salary = 0
        self.basic_salary = employee.get_employee_details()['basic_salary']
    
    def calculate_gross_salary(self):
        self.hra = (self.basic_salary * 20) / 100
        self.da = (self.basic_salary * 10) / 100
        self.gross_salary = self.basic_salary + self.hra + self.da
    
    def get_salary_details(self):
        self.calculate_gross_salary()
        return {
            'basic_salary' : self.basic_salary,
            'hra' : self.hra,
            'da' : self.da,
            'gross_salary' : self.gross_salary
        }
        
class DeductionsCalculator:
    def __init__(self, gross_salary_fetcher):
        self.salary_details = gross_salary_fetcher.get_salary_details()
        self.tax = 0
        self.pf = 0
        self.gross_salary = self.salary_details['gross_salary']
        self.basic_salary = self.salary_details['basic_salary']
        self.net_salary = 0
    
    def calculate_deductions(self):
        self.tax = (self.gross_salary * 10) / 100
        self.pf = (self.basic_salary * 5) / 100
        
    def net_salary_calculator(self):
        self.net_salary = self.gross_salary - self.tax - self.pf
        
    def get_deductions_and_net_salary(self):
        self.calculate_deductions()
        self.net_salary_calculator()
        return {
            'tax' : self.tax,
            'pf' : self.pf,
            'net_salary' : self.net_salary
        }
        
class PayslipGenerator:
    def __init__(self, employee, gross_salary_fetcher, deduction_calculation_executor):
        self.deductions_and_net_salary = deduction_calculation_executor.get_deductions_and_net_salary()
        self.salary_details = gross_salary_fetcher.get_salary_details()
        self.employee_details = employee.get_employee_details()
        
    def generate_payslip(self):
        return f'''
=== Payslip for {self.employee_details['name']} ===

-- Employee Details --
Employee Id: {self.employee_details['id']} 
Employee Department: {self.employee_details['department']}

-- Salary Details --
Basic Salary: {self.salary_details['basic_salary']}
HRA: {self.salary_details['hra']}
DA: {self.salary_details['da']}

-- Gross Salary --
Gross Salary: {self.salary_details['gross_salary']}

-- Deductions --
Tax: {self.deductions_and_net_salary['tax']}
Provident Fund: {self.deductions_and_net_salary['pf']}

-- Net Salary --
Net Salary: {self.deductions_and_net_salary['net_salary']}
'''

class Notification:
    def __init__(self, name):
        self.name = name
        
    def send_notification(self):
        print(f'Sent Salary Notification to {self.name}')
        

class SavePayslip:
    def __init__(self, employee, payslip_generate_executer):
        self.payslip = payslip_generate_executer.generate_payslip()
        self.name = employee.get_employee_details()['name']
    
    def save(self):
        print(self.payslip)
        print('Payslip Saved to Database')
        # Just Simulating Saving Feature
                

employee = EmployeeDetails(1, 'Rudalph', 'Software Engineering', 40000)

gross_salary_fetcher = GrossSalaryCalculator(employee)

deduction_calculation_executer = DeductionsCalculator(gross_salary_fetcher)

payslip_generate_executer = PayslipGenerator(employee, gross_salary_fetcher, deduction_calculation_executer)

saving_executer = SavePayslip(employee, payslip_generate_executer)
saving_executer.save()

notify = Notification(employee.employee_name)
notify.send_notification()


