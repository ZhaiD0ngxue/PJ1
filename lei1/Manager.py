from lei1.Customer import Customer
from lei1.Employee import Employee

class Manager(Customer,Employee):
    def __init__(self,fa,add,sala):
        # super().__init__(fa,add)
        # super(Manager,self).__init__(fa,add)
        # super(Employee,self).__init__(sala)
        Customer.__init__(self,fa,add)
        Employee.__init__(self,sala)