# import random


# from random import randint
#
# print("Відгадайте число від 0 - 100 використовуючи підказки")
# unknown = int(input("Ведіть число для відгадування: "))
# a = random.randint(0, 100)
#
# count = 0
#
#
# while a != unknown:
#
#     count += 1
#     if unknown > a:
#         print("Введене число більше за загадане")
#
#
#     elif unknown < a:
#         print("Введене число менше за загадане")
#     unknown = int(input("Ведіть число для відгадування: "))
#
# else:
#     print(("Вітаємо ви відгадали число!" "\n" f" Спроб використано: {count}"))

import re

print("Пароль повинен містити літери латинського алфавіту"
      "нижнього та верхнього регістрів,як мінімум одну цифру"
      "та спец. символи як $#@")

password = input("Enter a password: ")

chek1 = re.findall("[a-z]", password)
chek2 = re.findall("[A-Z]", password)
chek3 = re.findall("\d", password)
chek4 = re.findall(r"$|#|@", password)

if 6 <= len(password) <= 16 and chek1 and chek2 and chek3 and chek4:
    print("Ваш пароль прийнято")
else:
    print("Введено якесь невірне значення")
