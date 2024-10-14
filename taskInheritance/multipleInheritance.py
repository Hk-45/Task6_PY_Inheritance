
#Multiple Inheritance

#Base class 1
class employee:

    empName = input('enter employee name : ')
    empAge = input('enter employee age : ')
    empCompany = input('enter employee company : ')
    
    def printInfo(self):
        print(f'Enter empName : {self.empName}')
        print(f'Enter empAge : {self.empAge}')
        print(f'Enter empCompany : {self.empCompany}')

        
#Base class 2
class Hr:

    HrName = input('enter HR name : ')
    HrDept = input('enter HR dept : ')

    def printHrINfo(self):
        print(f'Enter HrName : {self.HrName}')
        print(f'Enter HrDept : {self.HrDept}')


#Derived class which access the base class 1 and 2
class company(employee,Hr):

    def compInfo(self):
        print()
        
        print(f'employee Name : {self.empName}')
        print(f'employee Age : {self.empAge}')
        print(f'employee Company : {self.empCompany}')
        print(f'HR name : {self.HrName}')
        print(f'HR dept : {self.HrDept}')



objCmp = company()

objCmp.compInfo()