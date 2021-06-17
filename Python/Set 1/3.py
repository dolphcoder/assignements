#3
class Display:
    def getString(self):
        self.str1 = input('Enter string: ')
    
    def printString(self):
        print(self.str1.upper())

d = Display()
d.getString()
d.printString()
