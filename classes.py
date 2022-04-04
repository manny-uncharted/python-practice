# Python Object-Oriented Programming

class Employee:

    raise_amt = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self): # Used for logging and debugging
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    
    def __str__(self): # Used for display to users
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): # a dunder method that adds salaries of staff
        return self.pay + other.pay

    def __len__(self): # a dunder method that prints the length of employee fullname
        return len(self.fullname())



    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # calling the parent init method
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else: 
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        

emp_1 = Employee('Manuel','Akanji',50000)
emp_2 = Employee('Test','User',60000)


"""When we try to access an attribute the on an instance it would first check if the instance contains that attribute,
    and if it doesn't it would see whether that class or any class it inherits from contains that attribute"""

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

"""printing the namespace of emp_1 and Employee class"""
# print(emp_1.__dict__)
# print(Employee.__dict__)

"""Printing the email attribute of the employee class"""
# print(emp_1.email)
# print(emp_2.email)

"""Printing the fullname method of the class employee making easier to call the fullname when needed"""
# print(emp_1.fullname())
# emp_1.fullname()
# Employee.fullname(emp_1)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

"""Printing a class variable that increments on the class Employee."""
# print(Employee.num_of_emps)

"""Differences between regular methods, static methods and class methods
    Regular methods: Take in the instance as the first argument "self"
    Class methods:You just add a class decorator and it takes "cls"
"""

"""Working with class methods"""
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

"""
Using class methods as alternative constructors, using these to provide multiple ways of creating our object
"""
# emp_str_1 = 'John-Doe-30000'
# emp_str_2 = 'Steve-Brown-70000'
# emp_str_3 = 'Mike-Smith-40000'

# new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

"""
Using static method: They don't pass the instance or the class as arguments in the function. When to use static method is when you are not using the self method or class method in it
"""

# import datetime
# my_date = datetime.date(2016, 7, 10)

# print(Employee.is_workday(my_date))


"""Class Inheritance"""
# dev_1 = Developer('Manny','Samuel',50000, 'Python')
# dev_2 = Developer('Testing','User2',60000, 'Java')


# mgr_1 = Manager('Sue', 'Sam', 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2) # Add employee to manager

# mgr_1.remove_emp(dev_1) # Remove employee

# mgr_1.print_emps()

"""Helps to show method resolution order"""
# print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

"""Check if an object is an instance of a class"""
# print(isinstance(mgr_1, Employee))

"""Check if an object is a subclass of a class"""
# print(issubclass(Manager, Employee))




"""Special and Magic/Dunder Methods """
# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(emp_1 + emp_2)

# print(len(emp_1))  

