#  LISTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# dem_list_1 = ['Orange', 'Mango', 2, False]
# dem_list_2 = [1, 2, 3, 4, 5, 6]
# dem_list_3 = [True, False, True, False]

# print(dem_list_1)
# print(dem_list_1[0])
# print(dem_list_1[0:2])
# print(dem_list_1[3])
# # Append - adds value to the right end cornor
# dem_list_1.append('Yellow')
# print(dem_list_1)

# #  INSERT - adds value in the said possition as follows
# # ANY VALUE WHICH IS IN THE SAME LOCATION WOULD BE SHIFTED FORWARD.
# dem_list_1.insert(4, 'Kenta')
# print(dem_list_1)

# # Remove
# dem_list_1.remove(2)
# print(dem_list_1)

# # REMOVE EVERYTHING BY - clear

# # dem_list_3.clear()
# print(dem_list_3)

# POP - removes last element out of the list

# dem_list_1 = ['Orange', 'Mango', 2, False]
# dem_list_2 = [51, 100, 12, 32, 53, 64, 75, 86]
# dem_list_3 = [True, False, True, False]

# dem_list_2.pop()
# print(dem_list_2)
# m0 = dem_list_2.index(32)
# # print(dem_list_2.index(32))
# # WORKES
# print(m0)

#  COUNT

# dem_list_4 = [1, 1, 1, 51, 100, 12, 32, 53, 64, 75, 86]

# print(dem_list_4.count(1))

# #  SORT
# dem_list_4.sort()
# print(dem_list_4)
# #  REVERSE >>>>>>>>>> IF SORT is not run or added in the function b4 this
# # It will reverse the values as mentioned in the first (VARIABLE).
# dem_list_4.reverse()
# print(dem_list_4)

#  COPY

# just_Copy = ['Anna', 'Tien', 'Zara', 'etc']

# j_C = just_Copy.copy()
# print(j_C)

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