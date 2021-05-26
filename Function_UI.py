import module_functions


def wick_UI():
    print("1. Прямокутник, 2. Трикутник, 3.Коло")

    while True:
        a = int(input("Оберіть площу якої фігури  ви хочите обрати: "))
        if a == 1:
            x = float(input("x"))
            y = float(input("y"))
            print (module_functions.squer (x,y))
        elif a == 2:
            h = float(input("h"))
            a = float(input("a"))
            print(module_functions.triangle(h,a))
        elif a == 3:
            print(module_functions.circle(float(input("r"))))

        elif a == 4:
            print("over")
            break

        else:
            print("Введіть коректне значення")
    else:
        print("кінець роботи")



print(wick_UI())