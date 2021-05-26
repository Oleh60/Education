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

class User:

    def __init__(self, first_name, last_name, place_of_birth, home_town,login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.place_of_birth = place_of_birth
        self.home_town = home_town
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name, self.last_name)

    def greeting_user(self):
        print(f"Hello, {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


men = User("Stepan", "Pukalo", "Lviv", "Lviv")
# men.describe_user()
# men.greeting_user()
for i in range(3):
    men.increment_login_attempts()
print(men.login_attempts)
men.reset_login_attempts()
print(men.login_attempts)

class Admin(User):

    def __init__(self,first_name, last_name, place_of_birth, home_town,privileges,login_attempts = 0):
        User.__init__(self,first_name, last_name, place_of_birth, home_town,login_attempts)
        self.privileges = privileges



    def greeting_user(self):
        print(f"Hello Administrator: {self.first_name}")

# adm1 = Admin("Stepan1", "Pukalo", "Lviv", "Lviv")
#
# adm1.show_privileges()
# adm1.describe_user()
# adm1.greeting_user()
# men.greeting_user()


class Privileges:

    def __init__(self,privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]):
        self.privileges = privileges

    def show_privileges(self):
        for item in self.privileges:
            print(item)
priv = Privileges()
admin = Admin("Stepan2","Pukalo2","Lviv","Lviv",priv)
admin.privileges.show_privileges()

