#https://edabit.com/challenge/j2HauiSdDadkjxjsQ

class Employee:
    
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    @classmethod
    def from_string(cls, s):
        firstname, lastname, salary = s.split('-')
        return cls(firstname, lastname, int(salary))
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")
emp3 = Employee.from_string("Susan-Walker-70000")
emp4 = Employee.from_string("Michael-Ferry-90000")
emp5 = Employee("Graham", "Derrell", 55000)

print(emp1.firstname)