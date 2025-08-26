class employee :
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def info_(self):#that is the instance of class employee
        info=f"the name is {self.name} and the salary is {self.salary}."   
        print(info)
    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def print_company(cls,company):
        print(cls.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company    
        

e1=employee("john",34000)
e1.info_()
print(e1.sum(3,45)) 
e1.change_company("acer")
print(employee.company)