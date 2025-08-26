class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):#double underscore is used in dunder method
        return f"the name of employee is {self.name} and the salary is {self.salary}" 
    def __repr__(self):
        return f"name:{self.name}\nsalary:{self.salary}"
    
e1=employee("neelesh", 34000)
print(e1.name)
print(e1.__str__())  
print(e1.__repr__())     