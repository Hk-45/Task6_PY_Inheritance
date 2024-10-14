
#MultiLevel Inheritance

#Base Class
class company:

    def __init__(self):

        self.compName = input('Enter Company name: ')
        self.city = input('Enter Company city name: ')

        
# Intermediate class
class HR(company):

    def __init__(self):
        super().__init__()

        self.hrName = input('Enter HR name: ')
        self.hrDept = input('Enter HR department name: ')

        
#Derived Class 
class employee1(HR):

    def __init__(self):
        super().__init__()

        self.empName = input('Enter  employee Name: ')
        self.empCity = input('Enter employee city: ')
        self.empExp = input('Enter employee experience: ')

    
    
    def printInfo(self):
        print()
        print(f'Company Info')
        print(f'Enter company name : {self.compName}')
        print(f'Enter company city : {self.city}')
        print()
        print('HR info')
        print(f'Enter HR name : {self.hrName}')
        print(f'Enter HR department name : {self.hrDept}')
        print()
        print('employee info')
        print(f'Enter employee name : {self.empName}')
        print(f'Enter city name : {self.empCity}')
        print(f'Enter exp year : {self.empExp}')
        




objInfo = employee1()

objInfo.printInfo()