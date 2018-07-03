# Question:
# With a given integral number n, write a program to generate a dictionary that contains
# (i, i*i) such that is an integral number between 1 and n (both included). and
#  then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# def main():
#     n = int(input("Enter the integral number"))
#     d = {i : i*i for i in range(1,n+1)}
#     print(d)
#
# if __name__=='__main__':
#     main()
########################################################################################
# Question:
# Write a program which accepts a sequence of
# comma-separated numbers from console and generate a list
#  and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# numbers = input("Enter the numbers")
# l = list(numbers.split(','))
# print(l)
# t = tuple(numbers.split("-"))
# print(t)

n = "as"

#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


# class UserClass:
#     def __init__(self,string_data=None):
#         self.string_data = string_data
#
#     def getString(self):
#         self.string_data = input("Enter the input")
#
#     def printString(self):
#         return self.string_data.upper()
#
# u = UserClass()
# u.getString()
# print(u.printString())
#


n = 10

# Question:
# Write a program that calculates and
# prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program
#  in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence
# is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24


# def custom_eqtn(D, C=50, H=30):
#     # D = 1,2,3,4
#     Q = []
#     d_list = D.split(',')
#     d_list = [int(char) for char in d_list]
#     print(d_list)
#     for d in d_list:
#         Q.append(math.sqrt([(2* C * float(d)) / H]))
#     print(Q)
#
#
# #
# # d_data = input("Enter the value for D> ")
#
# custom_eqtn('100,150,180')
n1 = 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input
# and generates a 2-dimensional array. The element value
# in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


# def func(x,y):
#     array = [[i*j for j in range(y)] for i in range(x)]
#     print(array)
#
# func(3,5)
#

n2 = 3

# Question:
# Write a program that accepts a comma separated
# sequence of words as input and prints the words
#  in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# def sorting(l):
#     print(l)
#     list_data = l.split(',')
#     list_data.sort()
#     print(list_data)
#
#
# # print(list_data)
# # list_data = list(l.split('-'))
# # print(list_data)
# pass
#
# # data = input("Enter the CSV data > ")
# sorting('without,hello,bag,world')

n3 = 2

# A website requires the users to
# input username and password to register.
# Write a program to check the validity of password
# input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated
# passwords and will check them according to the above criteria.
#     Passwords that match the criteria are to be printed, each
# separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1


# def pass_decorator(func):
#     def wrapper(pass_list):
#         pos_pass = []
#         for password in pass_list:
#             if not re.search('[a-z]', password) or not \
#                     re.search('[0-9]', password) or not re.search('[A-Z]', password) \
#                     or not re.search('[$#@]', password) \
#                     or  len(password) < 6:
#                 print("Password not possible >", password)
#
#             else:
#                 pos_pass.append(password)
#                 pass
#         print(pos_pass)
#         return func(pos_pass)
#
#     return wrapper
#
#
# @pass_decorator
# def password(pass_list):
#     print(pass_list)
#
#
# pass_list = ['ABd1234@1', 'a F1#', '2w3E*', '2We3345']
# password(pass_list)

n = 1

# You are required to write a program to sort the (name, age, height)
# tuples by ascending order
# where name is string, age and height are numbers.
# The tuples are input by console
#  The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]




# import random
#
# row = int(input('Row:> '))
# col = int(input('Col:> '))
#
# random.seed(102)
#
# matrix = [[random.randint(0, 1) for c in range(col)] for r in range(row)]
#
# for i in range(row):
#     for j in range(col):
#         if i==0:
#             if j==0:
#                 if matrix[i,j] == matrix[]









if __name__ == '__main__':
    pass



















