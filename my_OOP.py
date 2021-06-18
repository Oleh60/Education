# class Car:
#
#     def __init__(self, name, kind, model):
#         self.name = name
#         self.kind = kind
#         self.model = model
#
#     def start(self):
#         print(f"Engine of car {self.name} started")
#
#     def stop(self):
#         print(f"Engine of car {self.name} stoped")
#
#     @staticmethod
#     def new_object():
#         return Car("Dewww","Lanos", "2")
#
#
# c1 = Car("Mitsubishi", "Outlander", "2")
# c1.start()
# c2 = Car("Mazda", "3", "2005")
# c2.stop()
# c3 = Car.new_object()
# c3.start()
#
#
# class Truck(Car):
#     def __init__(self, name, kind, model, veight, range):
#         Car.__init__(self, name, kind, model)
#         self.veight = veight
#         self.range = range
#
#     def start(self):
#         print(f"Engine of Truck {self.name} started")
#
#
# t1 = Truck("Kamaz", "Samosval", "5535", "3,5 tones", "250km")
# t1.start()

# class Enimals:
#
#     def __init__(self,name,age):
#         self.__name = name
#         self.age  = age
#     @property
#     def name(self):
#         print("get name")
#         return self.__name
#     @name.setter
#     def name(self,value):
#         print("set name")
#         if not isinstance(value,str):
#             self.__name = "defolt"
#         else:
#             self.__name = value
#
# e1 = Enimals("Knopa","11")
# e2 = Enimals("Styopa","2")
# e1.name = "1"
# print(e1.name)
# print(e2.name)

# class Rectangle:
#
#    def rec_squer(a,b):
#        return a * b
#
# print(Rectangle.rec_squer(2,3))


#
# class Circle:
#     def __init__(self,R):
#         self.__R = R
#         self.PI = 3.14
#
#     def C_squer(self):
#         return self.PI * (self.R ** 2)
#
#     def C_len(self):
#         return 2 * self.PI * self.R
#
# c1 = Circle(8)
# print(c1.C_squer())
# print(c1.C_len())
# print(c1.R)

# class Print:
#
#     def __init__(self,message):
#         self.message = message
#
#     @staticmethod
#     def inputer():
#         a = input("Enter a message: ")
#         return Print(a)
#
#     def upperer(self):
#         print(self.message.upper())
#
# p1 = Print.inputer()
# p1.upperer


# from Shop import Shop
#
#
#
# store = Shop("Rozetka","Inet Shop")
# print(store.shop_name,store.shop_type)
# store.describe_shop()
# store.open_shop()
# store1 = Shop("Ibis","Gun Shop")
# store1.describe_shop()
# print(store.numbers_of_units)
# store.numbers_of_units = 100
# print(store.numbers_of_units)
# print(store.numbers_of_units)
# store.set_number_of_units(150)
# print(store.numbers_of_units)
# store.increment_number_of_units(10)
# print(store.numbers_of_units)
# all_store = Shop("Sadyba","garden store")
# all_store.describe_shop()
#
# class Discount(Shop):
#
#     def __init__(self,shop_name,shop_type,discount_products,number_of_units = 0):
#         Shop(shop_name,shop_type,number_of_units)
#         self.discount_product = discount_products
#
#     def get_discounts_products(self):
#         print(self.discount_product)
#
# store_discount = Discount("ATB","Grocery","Sosige",50)
# store_discount.get_discounts_products()

# class Bank:
#
#     def __init__(self,balance = 0):
#
#         self.__balance = balance
#
#
#     def deposit(self,cash):
#         self.__balance += cash
#         print(f"I deposite on your account: {self.__balance}")
#         print(f"On the account: {self.__balance}")
#
#     def withdraw(self,b):
#         print(f"I withdraw from your bank account: {b}")
#         if self.__balance - b > 0:
#             self.__balance -= b
#             print(f"On the account: {self.__balance}")
#         else:
#             print("Error: Not not enough money")
#
#
# acc = Bank()
# acc.withdraw(100)
# acc.deposit(1000)
# acc.withdraw(50)

# class User:
#
#     def __init__(self, first_name, last_name, place_of_birth, home_town,login_attempts = 0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.place_of_birth = place_of_birth
#         self.home_town = home_town
#         self.login_attempts = login_attempts
#
#     def describe_user(self):
#         print(self.first_name, self.last_name)
#
#     def greeting_user(self):
#         print(f"Hello, {self.first_name}")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# men = User("Stepan", "Pukalo", "Lviv", "Lviv")
# # men.describe_user()
# # men.greeting_user()
# for i in range(3):
#     men.increment_login_attempts()
# print(men.login_attempts)
# men.reset_login_attempts()
# print(men.login_attempts)
#
# class Admin(User):
#
#     def __init__(self,first_name, last_name, place_of_birth, home_town,privileges,login_attempts = 0):
#         User.__init__(self,first_name, last_name, place_of_birth, home_town,login_attempts)
#         self.privileges = privileges
#
#
#
#     def greeting_user(self):
#         print(f"Hello Administrator: {self.first_name}")

# adm1 = Admin("Stepan1", "Pukalo", "Lviv", "Lviv")
#
# adm1.show_privileges()
# adm1.describe_user()
# adm1.greeting_user()
# men.greeting_user()


# class Privileges:
#
#     def __init__(self,privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         for item in self.privileges:
#             print(item)
# priv = Privileges()
# admin = Admin("Stepan2","Pukalo2","Lviv","Lviv",priv)
# admin.privileges.show_privileges()
#

##### Less 2#####


# class Human:
#
#     def __init__(self,name):
#         self.name = name
#
#     def welcome(self):
#         print(f"Hello {self.name}")
#
#     def homosapiens(self):
#         return f"{self.name} is  Homosapiens"
#
#     @staticmethod
#     def random_massage():
#         return "Jesus is a rockstar"
#
#     @staticmethod
#     def createHuman():
#         return Human("new name")

# human = Human("Oleksandr")
# human.welcome()
# print(Human.homosapiens())
# print(Human.random_massage())
# h1 = Human.createHuman();
# h1.welcome()
# counter = 0
# class Worker:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         global counter
#
#         counter += 1
#         self.id = counter
#
#     @staticmethod
#     def quantity():
#         print(f"Total quantity of workers is: {counter}")
#
#
#     def workers(self):
#         print(self.id,self.name, self.salary)
#
#     @staticmethod
#     def info():
#         print(Worker.__base__,Worker.__dict__,Worker.__name__,Worker.__module__,
#               Worker.__doc__)
#
#
#
# work = Worker("Ahmed", "Salary is: 1500$ and sheep")
# work1 = Worker("Abdul", "Salary is: 30$")
# Worker.quantity()
# work.workers()
# work1.workers()
# Worker.info()
### Less 3 ###

# import random
#
# class Coin:
#
#     def __init__(self,):
#         self.__sideup = sideup
#
#     def toss(self):
#

# class Car:
#
#     def __init__(self, brand, model, year_of_make, speed=0):
#         self.brand = brand
#         self.model = model
#         self.year_of_make = year_of_make
#         self.speed = speed
#
#         print(f"Characteristic of the car:  {brand},{model},{year_of_make}")
#
#     def accelerate(self):
#         self.speed += 5
#         if self.speed > 0:
#             print(f"Car accelerate to: {self.speed} Km\H ")
#         self.get_speed()
#
#     def brake(self):
#         self.speed -= 5
#         if self.speed == 0:
#             print("Car stopped")
#         elif self.speed < 0:
#             print(f"Its revers speed: {self.speed}")
#
#         if self.speed > 0:
#             print(f"Car slowdown to : {self.speed} Km\H ")
#
#         self.get_speed()
#
#     def get_speed(self):
#         print(f"Current speed is {self.speed}")
#
#
# car = Car("Mitsubishi", "Outlander", "2008")
# car.accelerate()
# car.accelerate()
# car.accelerate()
# car.accelerate()
# car.accelerate()
# car.brake()
# car.brake()
# car.brake()
# car.brake()
# car.brake()
# car.brake()
# car.brake()brake
#

# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.curent = 0
#         # Конструктор з аргументом - місткість скарбнички
#
#     def can_add(self, v):
#         if self.capacity >= self.curent + v:
#             return True
#         return False
#
#
#         # True, якщо можна додати v монет, False інакше
#
#     def add(self, v):
#         if self.can_add(v):
#             self.curent += v
#             return (True)
#         else:
#             return (False)
#         # Покласти v монет в скарбничку
#
# money = MoneyBox(10)
# while True:
#
#     result  = money.add(int(input("Put a money on a box: ")))
#     if result == False:
#         print("Not enough space")
#         break


# class Dog:
#
#     def __init__(self,mammal,nature,breed,name,age):
#         self.mammal = mammal
#         self.nature = nature
#         self.breed = breed
#         self.name = name
#         self.age = age
#
#
#     def info(self):
#         print(f"{self.name} is: {self.age}")
#
#     def bark(self):
#         print(f"{self.name} can dance")
#         print(f"{self.name} can give a paw")
#
# class German_shepard(Dog):
#
#     def __init__(self,mammal,name,age):
#         self.breed = "German_shepard"
#         self.nature = "lapukh"
#         Dog(mammal,self.nature,self.breed,name,age)
#
#     def bark(self):
#         print(f"{self.breed} can bark on wolfs")
#
#     def get_nature(self):
#         print(f"{self.nature} nordicheskii")
#
# class Pets:
#
#     def __init__(self):
#         self.count = 0
#         self.pets = []
#
#     def add_to_pets(self,object):
#         self.count += 1
#         self.pets.append(object)
#         return self
#
#     def get_info(self):
#         if self.count == 1:
#             print(f"You have {self.count} pet ")
#         else:
#             print(f"You have {self.count} pets ")
#         for i in self.pets:
#             print(i.age)
#
# pet = Dog("Mammal","Ragul","German Shepard","Pitukh","8")
# pet1 = German_shepard("Mammal","Zalupa","4")
# pet.bark()
# pet1.bark()
# pets = Pets().add_to_pets(pet).add_to_pets(pet1).get_info()





