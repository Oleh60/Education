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


while True:
    login = input("enter a login: ")
    if login == "First":
        print("Hello user")
        break
    else:
        print("not correct login")











