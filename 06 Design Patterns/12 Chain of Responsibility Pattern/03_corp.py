'''
A very common and standard example of the Chain of Responsibility Design Pattern is:
Expense Approval System.

Example: Expense Approval System
Imagine an employee wants reimbursement for a business expense.

Different managers have different approval limits:
Handler	Maximum amount they can approve
Team Lead: ₹5,000
Manager: ₹20,000
Director: ₹1,00,000
'''

from abc import ABC, abstractmethod

class ExpenseHandler(ABC):
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler

    @abstractmethod
    def approve(self, amount):
        pass


class TeamLead(ExpenseHandler):
    def approve(self, amount):
        if amount <= 5000:
            print("Team Lead approved the expense.")
        elif self.next:
            self.next.approve(amount)
        else:
            print("Expense cannot be approved.")


class Manager(ExpenseHandler):
    def approve(self, amount):
        if amount <= 20000:
            print("Manager approved the expense.")
        elif self.next:
            self.next.approve(amount)
        else:
            print("Expense cannot be approved.")


class Director(ExpenseHandler):
    def approve(self, amount):
        if amount <= 100000:
            print("Director approved the expense.")
        else:
            print("Expense cannot be approved.")


# Creating handlers
team_lead = TeamLead()
manager = Manager()
director = Director()

# Creating chain
team_lead.set_next(manager)
manager.set_next(director)

# Sending requests
team_lead.approve(3000)
team_lead.approve(15000)
team_lead.approve(50000)
team_lead.approve(150000)
