from lei1.Customer import Customer
from lei1.Employee import Employee

class Manager(Customer,Employee):
    def __init__(self,fa,add,sala,age):
        Customer.__init__(self,fa,add)
        Employee.__init__(self,sala)
        self.age=age