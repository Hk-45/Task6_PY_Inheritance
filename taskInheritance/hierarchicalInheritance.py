
#Hierarchical Inheritance

#Base class 
class store:

    def superMarket(self):
        print('Welcome in super Market')

#Derived class 1
class product1(store):

    def prod1(self):
        self.prodName = input('Enter 1st product name: ')
        self.prodPrice = input('Enter 1st product price: ')


        print(f'product name : {self.prodName}')
        print(f'product price : {self.prodPrice}')
        print()


#Derived class 2
class product2(store):

    def prod2(self):
        self.prodName2 = input('Enter 2nd product name: ')
        self.prodPrice2 = input('Enter 2nd product price: ')

        print(f'product name : {self.prodName2}')
        print(f'product price : {self.prodPrice2}')
        print()


#Derived class 3
class product3(store):

    def prod2(self):
        self.prodName3 = input('Enter 3rd product name: ')
        self.prodPrice3 = input('Enter 3rd product price: ')

        print(f'product name : {self.prodName3}')
        print(f'product price : {self.prodPrice3}')


obj1 = product1()
obj2 = product2()
obj3 = product3()
obj1.superMarket()
obj1.prod1()

obj2.prod2()

obj3.prod3()
