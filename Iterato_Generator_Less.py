
# list1 = ["1","2","3","4","5","7"]
# a = []
# for i in list1:
#     a.append(int(i))
# print(a)

# mapped_numbers = list(map(lambda x: int(x),list1))
# print(mapped_numbers)

# miles = [1,15,60]
# def convert(mile):
#     return mile * 1.6
# print(list(map(convert,miles)))
#
#
# print(list(map(lambda x: x * 1.6, miles)))

# import functools
#
# list2 = [1,2,57,33,566,22,98,986]
#
# print(functools.reduce(lambda x,y: x if x > y else y,list2))

# def generator_r():
#     curent = 1
#     while True:
#         yield curent
#         curent += 1
# range = generator_r()
# print(next(range))
# print(next(range))
# print(next(range))
# print(next(range))
# print(next(range))