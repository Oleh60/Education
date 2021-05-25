# a = int(input("введіть число А"))
# b = int(input("Введіть число Б"))
# if a > b:
#     print(f"Число {a} більше за Б")
# elif a < b:
#     print(f"Число {b} більше за А")
# elif a == b:
#     print("Числа А та Б рівні між собою")

# number = int(input("enter number: "))
#
# if number %2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# start = 0
# finish = 100
# while start < finish:
#     start +=2
#     print(start)
# else:
#     print("the end")
#
#
# for value in range(101):
#     if value % 2 == 0:
#         print(value, end = " ")

# number = int(input("Enter a Factorial number"))
# b = 1
# for i in range(1,number):
#     b *= i
# print(b)

# mass = [5,10,15,20]
# for i in mass:
#     print(float(i))

# n = int(input("Enter a namber: "))
# a = 0
# b = 1
#
# while True:
#     print(a)
#     c = a+b
#     if c > n:
#         break
#     a = b
#     b = c

# print("enter quntity that the same as first number")
# user_number = int(input("enter a number: "))
#
# a = []
#
# for item in range (user_number):
#     a.append(int(input("enter a next number: ")))
# print(min(a),max(a))

# w = [int(input("enter a next number: ")) for item in range(int(input("enter a  number: ")))]
# print(min(w),max(w))

# for i in range(1,11):
#     if i % 2 == 0:
#          print(i, "число ділиться на 2")
#     elif i % 3 == 0:
#         print(i, "число ділиться на 3")
#     elif i % 2 == 1 and i % 3 == 1:
#         print(i,"число не ділиться на 2 і 3")


# while True:
#     login = input("enter a login: ")
#     if login == "First":
#         print("Hello user")
#         break
#     else:
#         print("not correct login")

# def arifmetic_mean(*args):
#     return sum(args) /len(args)
#
# print(arifmetic_mean(5,4,3))

# def largest_number(a,b):
#     """a function will retur largest number"""
#     if a > b:
#         return a
#     else:
#         return b
# print(largest_number.__doc__)

# def sq_of_rectangle():
#     a = int(input("enter lengt of side a:"))
#     b = int(input("enter lengt of side b:"))
#     print("square of rectangle")
#     return  a * b


# def sq_of_triangle():
#     a = int(input("enter lengt of side a: "))
#     b = int(input("enter lengt of side b: "))
#     c =int(input("enter lengt of side c: "))
#     p = (a+b+c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
#     print("square of triangle")
#     return S
#
# def sq_of_circle():
#     r =int(input("enter a radius: "))
#     PI = 3.14
#     print("square of circle")
#     return PI*r ** 2
#
# while True:
#     print("Enter 1 for rectangle")
#     print("Enter 2 for triangle")
#     print("Enter 3 for circle")
#     print("Enter 4 for exit")
#     i = input("\n \t")
#     if i == "1":
#         print(sq_of_rectangle())
#     elif i == "2":
#         print(sq_of_triangle())
#     elif i == "3":
#         print(sq_of_circle())
#     elif i == "4":
#         break
#     else:
#         print("You inputed incorrect symbol")
#     input("press Enter to continue")

# def string_len(str):
#     print(len(str))
#
# string_len(input("Enter a random string"))


##################
#Modules
##################


def square_digits(num):
    a = str(num)
    b = []
    for i in a:
        b.append(str(int(i) ** 2))
    return int("".join(b))
print(square_digits(9119))
