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

def task4():
    a = int(input("введіть довжину сторони А: "))
    b = int(input("Введіть довжину сторони В: "))
    s = (a*b / 2)
    print("Площа трикутника = %.2f"% s)
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
def task12():
    a = input("Enter a number: ")
    b = list(a)
    i  = len(b)
    while i > 3:
        i -= 3
        b.insert(i,",")
    print('' .join(b))


task12()








