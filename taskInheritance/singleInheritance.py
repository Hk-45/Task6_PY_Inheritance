# Single Inheritance

import re

#parent class
class checkText:

    def __init__(self):
        self.EnterText = input('Enter any Text : ')

    def printText(self):
        print(f'text = {self.EnterText}')   

#child class
class removeText(checkText):

    def __init__(self):
        super().__init__()

    def onlyNum(self):
        self.Number = re.sub('[^0-9]','',self.EnterText)

        print(f'text = {self.EnterText}')
        print(f'Only numbers from text = {self.Number}')
   

objRe = removeText()

objRe.onlyNum()
