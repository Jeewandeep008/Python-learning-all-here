# identify the data type in python
# type() function
from math import *
# https://www.w3schools.com/python/python_syntax.asp

# SOME ARE REPETED

bo = (1,2,3,4,5,6,7,8,9,10)
print(type(bo))
print('_________',bo,'___________')
bo_1 = 'Jeewan'
print(type(bo_1))
print('_________',bo_1,'___________')
bo_2 = ['Jeewan', 'Deep', 'Tete']
print(type(bo_2))
print('_________',bo_2,'___________')
bo_3 = {1,2,3,4,5,6,7,8,9,10}
print(type(bo_3))
print('_________',bo_3,'___________')
bo_4 = True
print(type(bo_4))
print('_________',bo_4,'___________')
bo_5 = {
    'Jan': 'January',
    'Feb': 'Febuary',
    'Mar': 'March',
}
print(type(bo_5))
print('_________',bo_5,'___________')
bo_6 = {"name" : "John", "age" : 36}
print(type(bo_6))
print('_________',bo_6,'___________')
bo_7 = 1j
print((type(bo_7)))
print('_________',bo_7,'___________')
bo_8 = 20.5
print((type(bo_8)))
print('_________',bo_7,'___________')
bo_9 = 20
print(type(bo_9))
print('_________',bo_8,'___________')
bo_10 = frozenset({"apple", "banana", "cherry"})
print(type(bo_10))
print('_________',bo_9,'___________')
bo_11 = range(10)
print(type(bo_11))
print('_________',bo_10,'___________')
bo_12 = b"Hello"
print(type(bo_12))
print('_________',bo_11,'___________')
bo_13 = bytearray(5)
print(type(bo_13))
print('_________',bo_12,'___________')
bo_14 = memoryview(bytes(5))
print(type(bo_14))
print('_________',bo_13,'___________')