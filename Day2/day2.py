# -*- coding: utf-8 -*-
"""Day2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lTB-g4We2OwbwObKLsLDV4jKrECWzy0u

### **Assignment**

Q1. Name the keyword which helps in writing code involving conditions.**bold text**

Answer -> if else
"""

# Example - To know odd and even

user_input = int(input())

if user_input % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

"""Q2. Write the syntax of a simple if statement.

if expression(boolean):
      code to execute
    elif expression(boolean):
      code to execute
    else:
      code to execute
"""

# calculator problem
num1, num2 = input('Enter two number seperated by space: ').split(' ')
num1 = int(num1)
num2 = int(num2)
print('Enter the operator choice number from below\n\t1. Sum\n\t2. Difference\n\t3. Multiply\n\t4. Division')
choice = input('Enter your choice: ')
if choice == '1':
  print(num1 + num2)
elif choice == '2':
  print(num1 - num2)
elif choice == '3':
  print(num1 * num2)
elif choice == '4':
  print(num1 / num2)

"""Q3. Write a program to check whether a person is eligible for voting or not. (accept age from user)"""

# voters in India have right to vote if they are 18+
age = int(input())
if age >= 18:
  print('You can vote as you are 18+')
else:
  print("You can't vote as you are not even 18. You need to wait for {} year(s) more.".format(18 - age))

"""Q4. What is the output of the given below program?

if 1 + 3 == 7:
      print("Hello")
    else:
      print("Know Program")

# *Output*

Know Program
"""

if 1 + 3 == 7:
    print("Hello")
else:
    print("Know Program")

"""Q5. Write a program to check whether a number entered by user is even or odd."""

user_input = int(input())

if user_input % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

"""Q6. Python program to find the largest element among three Numbers ?

num1 = 10 
    num2 = 50 
    num3 = 15
"""

#num1 = int(input())
#num2 = int(input())
#num3 = int(input())

num1 = 10
num2 = 50
num3 = 15

if (num1 > num2) and (num1 > num3):
  print("{} is the largest number".format(num1))
elif (num2 > num1) and (num2 > num3):
  print("{} is the largest number".format(num2))
elif (num3 > num2) and (num1 < num3):
  print("{} is the largest number".format(num3))

"""07. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on

"""

month_entered = int(input())
month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

if month_entered == 1:
  print("January")
elif month_entered == 2:
  print("Februrary")
  print("The month has 28/29 days.")  
elif month_entered == 3:
  print("March")
elif month_entered == 4:
  print("April")
elif month_entered == 5:
  print("May")
elif month_entered == 6:
  print("June")
elif month_entered == 7:
  print("July")
elif month_entered == 8:
  print("August")
elif month_entered == 9:
  print("September")
elif month_entered == 10:
  print("October")
elif month_entered == 11:
  print("November")
elif month_entered == 12:
  print("December")
else:
  print("Please enter from 1-12.")


if month_entered in month_31:
  print("The month has 31 days.")
elif month_entered in month_30:
  print("The month has 30 days.")



month_entered = int(input())
month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]

if month_entered == 1:
  print("January")
elif month_entered == 2:
  print("Februrary")
  print("The month has 28/29 days.")  
elif month_entered == 3:
  print("March")
elif month_entered == 4:
  print("April")
elif month_entered == 5:
  print("May")
elif month_entered == 6:
  print("June")
elif month_entered == 7:
  print("July")
elif month_entered == 8:
  print("August")
elif month_entered == 9:
  print("September")
elif month_entered == 10:
  print("October")
elif month_entered == 11:
  print("November")
elif month_entered == 12:
  print("December")
else:
  print("Please enter from 1-12.")


if month_entered in month_31:
  print("The month has 31 days.")
elif month_entered in month_30:
  print("The month has 30 days.")









