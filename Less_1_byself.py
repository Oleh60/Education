# a = int(input("Введіть число А: "))
# b = int(input("Введіть число В: "))
# c = int(input("Введіть число С: "))
# print(a + b + c)
# print(a * b * c)
# d = b - c
# print(a**d)

# n = int(input("Введіть число: "))
# a = n * 11
# b = n * 111
# print(n + a + b)

# name = ("Lord Voldemort")
# age = ("72")
# work = ("Magic")
# print(f"My name is {name} I am {age}and my hobby is {work}")

# def task4():
#     a = int(input("введіть довжину сторони А: "))
#     b = int(input("Введіть довжину сторони В: "))
#     s = (a*b / 2)
#     print("Площа трикутника = %.2f"% s)
# task4()

# a  = int(input("Enter a number: "))
# print(a - 1)
# print(a + 1)

# a = str(int(float(input("Enter a number: "))))
# print(a[len(a) -1])

# a = int(input("Enter a number that less than 100: "))
# if a <= 100:
#     print(2 ** a )
# else:
#     print("Enter correct number")

# a = str(int(float((input("Enter a number: ")))))
# if len(a) == 2:
#     print(a[0])
# def task12():
#     a = input("Enter a number: ")
#     b = list(a)
#     i  = len(b)
#     while i > 3:
#         i -= 3
#         b.insert(i,",")
#     print('' .join(b))


# task12()

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = ((a+b)*(a+b))
# print(c)


# a = float(input("Feets: "))
# b = float(input("Inches: "))
# c = round((a * 30.48) ++ (b * 2.54))
#
# print(c)

# a  = int(input("Input distance in feet: "))
# b = (a * 12)
# c = float(a * 0.333333333)
# d = float(a * 0.000189393939)
# print(f"The distance in inches is {b} inches. \n The distance in yards is {c} yards. \n The distance in miles is {d} miles."  )

# a = input("Enter a symbol: ")
# print(ord(a))

# a = int(input("Enter a symbol: "))
# print(chr(a))

# a = int(input("number1: "))
# b = int(input("number2: "))
# print(f"{a} + {b} = {a+b}")


# a = float(input("number1: "))
# print(round(a,3))

# a = (input("number1: "))
# for i in range(5 - len(a)):
#    a = '0'+a
# print(a)


# a = input("number1: ")
# for i in range(7 -len(a)):
#     a += '*'
# print(a)

# a = input("number1: ")
# print(a + "*" * (7- len(a)))

# a = int(input("days: "))
# b = int(input("hours: "))
# c = int(input("minutes: "))
# d = int(input("second: "))
# e = d + (c * 60)+(b * 3600)+(a*3600*24)
# print(e)

# a = float(input('Enter the desired future value: '))
# b = float(input("Enter the annual interest rate: "))
# c = float(input("Enter the number of years the money will grow: "))
# d = a/(1+b)*c
# print(round(d,3))

# a = input('enter number: ')
# b = input('enter number: ')
# c = input('enter number: ')
# print(c,b,a)

# a = int(input('enter number: '))
# b = int(input('enter number: '))
# print(a + b,a - b,a * b, a / b, a ** b,sep="&")

# a = int(input('enter number: '))
# b = int(input('enter number: '))
# c = b // a
# d = b - a * c
# print(f"{c} \n {d}")

# login = input("Enter a login: ")
# password = input("Enter a password: ")
# if login == "starLink" and password  == "12345":
#     print("You are loged")
# else:
#     print("Sorry, check youre login or password"

# a = []
# for i in range (int(input("enter count"))):
#     a.append(input("enter a name"))
# print(a)
# if a[0][0] > a[1][0]:
#     print(a[1],a[0])
# else:
#     print(a)
# i = 0
# while i < 6 :
#     a = int(input("enter a number"))
#     if a == 1:
#         print("one")
#     elif a == 2:
#         print("two")
#     elif a == 3:
#         print("three")
#
#     else:
#         print("Unknown")
#     i += 1

# a = []
# for i in range (2):
#     a.append(input("enter a letter "))
# print(a)
# if a[0][0] < a[1][0]:
#     print(a[1], "is not less than" ,a[0])
# else:
#     print(a)

# km_per_h = int(input("enter km: "))
# m_per_sec = int(input("enter meters:"))
# if km_per_h * 1000 / 3600 > m_per_sec:
#     print(km_per_h)
# else:
#     print(m_per_sec)