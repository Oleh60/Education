#
# inputer = int(input("Enter a odd number"))
# if inputer % 2 == 0:
#     print("The number is odd")
# else:
#     print("The number is even")

# try:
#     inputer = int(input("Enter a odd number: "))
#     if inputer % 2 == 0:
#         print(f"The {inputer} is even")
#     else:
#         print(f"The {inputer}  is odd")
# except ValueError as e:
#     print("Opps! it is a problem,pls try enter only a numbers")


# while True:
#     try:
#         inputer = int(input("Enter: "))
#         if inputer % 2 == 0:
#             print("even")
#         else:
#             raise ZeroDivisionError()
#     except ValueError:
#         print("error: number is str")
#
#     except ZeroDivisionError:
#         print("error: number is odd")
#
#     else:
#         break


# try:
#     a = int(input("Enter: "))
#     b = int(input("Enter: "))
#
#     res = a / b
# except ValueError:
#     print('value error')
#
# except ZeroDivisionError:
#     res = 0
#
# finally:
#     print(res)
#
# try:
#     inputer = input("Enter two  numbers: ")
#     inputer = inputer.split(",")
#     result = int(inputer[0]) / int(inputer[1])
# except ZeroDivisionError:
#     print("Dilyty na nol ne mozhna")
#     result  = 0
# except SyntaxError:
#     print("Syntax Error")
#
# except Exception:
#     print("Exeption")
#
# else:
#     print("Success")
#
# finally:
#     print("Program done")


# def age(age1):
#     try:
#
#         if age1 <= 0:
#             raise ZeroDivisionError
#         if age1 % 2 == 0:
#             return ("Your age number is even")
#         else:
#             return ("Your age number is odd")
#     except ZeroDivisionError:
#         return "Your number of age  is negative"
#     except Exception:
#         return "Opps! You enter wrong information"
#
# age1 = int(input("Enter your age: "))
#
# print(age(age1))


























