#Set 1

#1
# n = int(input("Enter n: "))8
# print({i:i**2 for i in range(1,n+1)})

#2
# l = input("Enter numbers separated by commas: ").split(',')
# print(l,"\n",tuple(l))

#3
# class Display:
#     def getString(self):
#         self.str1 = input('Enter string: ')
    
#     def printString(self):
#         print(self.str1.upper())

# d = Display()
# d.getString()
# d.printString()

#4   
# print(",".join(sorted(input("Enter the words separated by commas: ").split(","))))

#5
# print(tuple((x for x in (1,2,3,4,5,6,7,8,9,10) if x%2==0)))

#6
# from math import pi
# class Circle:

#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         print(pi*self.radius**2) 

# c = Circle(7)
# c.area()

#7
# email = input('Enter email address: ')
# print(email[:email.index('@')])

#8
# print(min(list(map(int, input('Enter the numbers: ').split()))))

#9
# import os
# lines_num, words_num, chars_num = 0,0,0
# with open('demotext.txt', 'r') as file:
#     for line in file:
#         lines_num += 1
#         words_num += len(line.split())
#         chars_num += sum([len(x) for x in line.split()])
# print('No of Lines: %d\nNo of Words: %d\nNo of Characters: %d' % (lines_num, words_num, chars_num))
