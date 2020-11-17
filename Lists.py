#  LISTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

list_1 = ['Orange', 'Mango', 'Ali', 'Tommy', 'Billu']
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_3 = [True, False, True, False]
list_4 = [1, 1, 1, 51, 100, 12, 32, 53, 64, 75, 86]

# print(type(list_1), type(list_2))
# print(list_1)
# print(list_1[0])
# print(list_1[0:2])
# print(list_1[3])

# print('_____','Length','_____')
# print(len(list_1))

# Change a list item
list_2[9] = 100
# print('_____','Change','_____')
# print(list_2)

# Change and insert more than 1 item
list_2[9] = [100, 110, 120]
# print('_____','Change with more objects','_____')
# print(list_2)

# Append
# adds value to the right end cornor
list_1.append('Yellow')
# # print('_____','Append','_____')
# print(list_1)

# #  INSERT
# To insert a new list item, without replacing
# any of the existing values, we can use the insert() method.
# adds value in the said position as follows
# # ANY VALUE WHICH IS IN THE SAME LOCATION WOULD BE SHIFTED FORWARD.
# list_1.insert(Target Index, 'New STRING or Number')
list_1.insert(4, 'Kenta')
# print('_____','Insert','_____')
# print(list_1)

# # Remove
# Should hae the vLUE PRESENT IN IT
list_1.remove('Ali')
# print('_____','Remove','_____')
# print(list_1)

# POP
# Removes last element out of the list when not specified
# list_2.pop(INDEX number)
list_2.pop()
# print('_____','POP','_____')
# print(list_2)
# print(list_2.pop(5)) # Removes - 6

# Clear
# # REMOVE EVERYTHING BY - clear
list_3.clear()
# print(list_3)

# INDEX
m0 = list_2.index(2)
# WORKES
# print(m0)

#  COUNT
# print('_____','COUNT','_____')
# print(list_4.count(1))

#  SORT
list_4.sort()
# print('_____','SORT','_____')
# print(list_4)

#  REVERSE >>>>>>>>>>
# IF SORT is not run or added in the function b4 this
# It will reverse the values as mentioned in the first (VARIABLE).
list_4.reverse()
# print('_____','Reverse','_____')
# print(list_4)

#  COPY
just_Copy = ['Anna', 'Tien', 'Zara', 'etc']
j_C = just_Copy.copy()
# print('_____','COPY','_____')
# print(j_C)

# EXTEND
# Add the elements of tropical to thislist:
extend_1 = ["apple","cherry"]
tropical = ["mango", "pineapple"]
# extend_1.extend(tropical)
tropical.extend(extend_1)
# print('_____','Extend','_____')
# print(extend_1) #not this
# print(tropical)

# Add Any Iterable - EXTEND
# The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).
# Example
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# print('_____','Add Any Iterable - EXTEND','_____')
# print(thislist)

# Delete list and Delete a part of list
# thislist_1 = ["apple", "banana", "cherry"]
# del thislist_1[0]
# print('_____','Delete a part of list','_____')
# print(thislist_1)

# and

# other_del = ["apple", "banana", "cherry"]
# del other_del
# https://www.w3schools.com/python/python_lists_comprehension.asp

# 2d list
new_list_2d = [ [1,2,3],[4,5,6],[7,8,9]]
# print(new_list_2d)
# print(new_list_2d[0])
# # print(new_list_2d[row no.][index no.])
# print(new_list_2d[0][0])
# print(new_list_2d[1])
# print(new_list_2d[1][1])
# print(new_list_2d[2])
# print(new_list_2d[2][2])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# TUPLE >>>>> CAN NOT MODIFY>> ITS LIKE A LIST BUT YET DIFFERENT >>>> COORDINATES

# example_of_tuple = (4, 55)
# print(example_of_tuple)

#  TypeError: 'tuple' object does not support item assignment
# example_of_tuple_1 = (4, 55)
# example_of_tuple_1[4] = 20
# print(example_of_tuple_1)

# Other exapmles >>> Combine List with Tuples >> still values can not be modified
# SO use it in cases when you do not wish to change the values

# ex_1 = [(5), ('Anna'), (4,5)]

# print(ex_1)
# print(ex_1[0])
# print(ex_1[1])
# print(ex_1[2])