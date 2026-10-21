'''
Question 1: Student Report Card System

You are building a simple system to manage student report cards.

The system should perform the following tasks:
    1. Store a student's name and marks in 3 subjects.
    2. Calculate the total marks and percentage.
    3. Determine whether the student has passed (percentage ≥ 40%).
    4. Display the student's report card in a readable format.

Your Task: Design and implement this system using classes while following the Single Responsibility Principle.
'''

class StudentInformation:
    def __init__(self, student_name, marks):
        self.studet_name = student_name
        self.marks = marks
        
    def get_name(self):
        return self.studet_name
    
    def get_marks(self):
        return self.marks

class CalculatePercentage:
    def __init__(self, student):
        self.student = student
    
    def calculate_percentage(self):
        percentage = 0
        marks = self.student.get_marks()
        for key, value in marks.items():
            percentage = percentage + value
            # Percentage implementation dosent matters. What matters is 'SRP' implementation
        return percentage
    
class FinalResult:
    def __init__(self, student):
        self.percentage_calculator = CalculatePercentage(student)
    
    def final_result(self):
        total_percentage = self.percentage_calculator.calculate_percentage()
        if total_percentage >= 40:
            return True
        else:
            return False
        
class DisplayReportCard:
    def __init__(self, student):
        self.student = student
        self.student_percentage_calculator = CalculatePercentage(self.student)
        self.student_final_result_displayer = FinalResult(self.student)
    
    def display_report_card(self):
        print(f'''
              Student Name: {self.student.get_name()}
              Student Marks: {self.student.get_marks()}
              Percentage: {self.student_percentage_calculator.calculate_percentage()}
              Status: {self.student_final_result_displayer.final_result()}
              ''')
        

student = StudentInformation("Rudalph", {'Physics':85, 'Chemistry':70, 'Maths':90})
reportCard = DisplayReportCard(student)
reportCard.display_report_card()
