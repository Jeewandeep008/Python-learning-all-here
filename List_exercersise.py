# Creating list the faster way
# Websites -https://www.programiz.com/python-programming/list-comprehension

# Normal way >>>>
# a = [1,2,3,4,5,6]
# print(a)
# print('len', len(a))
# print('index', a.index(1))
# print(a.index(6))
# x = map(, a)
# a = list(x)
# print(a)
# print(a.index(7)) # ValueError: 7 is not in list

# ab= ['Munna', 1, '2']
# print(len(ab))

# The normal for loop way >>>>>
# z1 = []
# for each_ii in range(11):
#     z1.append(each_ii)
# print(z1)
# Output
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# or >>>


# With string >>>>>>>>>>>>>
# fruits = ["apple", "banana", "cherry"]
# for each_list in fruits:
#     print(each_list)

# faster way if no. is 20 we will use range >>>>>>>>>>>>>>>
# l1 = [expression for val in collection]

# l1 = [val for val in range(6)]
# print(l1)

# convert integer like 1 to any number into list of string >>>>>>>>>>>>>

# convert_to_str = [i for i in range(6)]
# print(convert_to_str)
#
# convert_to_str_final = [str(i) for i in range(6)]
# print(convert_to_str_final)

# Convert a pre-written list with string into integer >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# https://www.kite.com/python/answers/how-to-convert-a-list-of-strings-to-ints-in-python
# USE map() TO CONVERT A LIST OF STRINGS TO INTS
# Use map(function, iterable) with a list of strings as iterable and int as function to
# apply int() to each string in the list.
# Use list(iterable) with the output of map() as iterable to convert to a list.

# om = ['2', '9', '8', '4', '9']
# new_om = map(int, om) #Maps each string to an int
# om = list(new_om) # Converts mapped output to a list of ints
# print(om)

# Even number >>> remender = 0
# m1 = [i for i in range(11) if i%2 == 0 ]
# print(m1)

# Odd number >>> remender = 1 e:g>> 2/2= remender 0 where as 3/2= remender = 1
# m2 = [i for i in range(11) if i%2 == 1 ]
# print(m2)

# FIND A VALUE IN A LIST USING FOR LOOP >>>>>>>>>>>>>>>>>>>>>> #

list_find_value = [i for i in range(11)]
# print(list_find_value)
list_find_value.append('exit')
# print(list_find_value)

# FIND THIS
n = 5
def bb(n):

    if n in list_find_value:
        print('Present -', str(list_find_value.index(n)))
    else:
        print('Absent')
# bb(n)