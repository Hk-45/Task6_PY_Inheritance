import re


class operations:

    def operation(self):
        print('Performing some operations')

class calculate(operations):

    def add(self,val1,val2):
        self.Value1 = int(val1)
        self.Value2 = int(val2)

        print(f'addition of {self.Value1} + {self.Value2} = {self.Value1 + self.Value2}')

class text(operations):

    def text(self):

        self.EnterText = input('Enter any text : ')



class removeText(calculate,text):

    def onlyNum(self):
        self.Number =  re.sub('[^0-9]','',self.EnterText)

        print(f'text = {self.EnterText}')
        print(f'result Number only = {self.Number}')

obj = removeText()

obj.operation()
obj.add(1,5)
obj.text()
obj.onlyNum()
