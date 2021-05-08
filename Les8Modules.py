import random
from random import randint

print("Відгадайте число від 0 - 100 використовуючи підказки")
unknown = int(input("Ведіть число для відгадування: "))
a = random.randint(0, 100)

count = 0


while a != unknown:

    count += 1
    if unknown > a:
        print("Введене число більше за загадане")


    elif unknown < a:
        print("Введене число менше за загадане")
    unknown = int(input("Ведіть число для відгадування: "))

else:
    print(("Вітаємо ви відгадали число!" "\n" f" Спроб використано: {count}"))


