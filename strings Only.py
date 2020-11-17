#STRINGS
# can refer to this - https://www.programiz.com/python-programming/methods/string/center
# https://www.w3schools.com/python/ref_string_index.asp

u = 'youtube'
# print(id(u))
# print(type(u))
# print(u)

# print(u[0:7])
# print(u[0])
# print(u[3])
# print(u[6])
# print('List is used to show the letters as list', list(u))
# print(len(u))
# print(u.index('youtube'))
# print(u.index('o'))

# INDEX
# string.index(value, start, end)
a1 = 'aaaebbcccccbe'

# print(id(a1))
# print('string.index(3, 0, 5) =', a1.index('e', 0, 5))
# print('string.index(3, 5, 15) =', a1.index('e', 5, 15))

# FIND()
# Example 1: find() With No start and end Argument

# quote = 'Let it be, let it be, lEt it be'
#
# # first occurance of 'let it'(case sensitive)
# result_1 = quote.find('lEt it')
# print("Substring 'let it':", result_1)
#
# # find returns -1 if substring not found as its not present in the string
# result_2 = quote.find('small')
# print("Substring 'small ':", result_2)
#
# # How to use find()
# if (quote.find('be,') != -1):
#     print("Contains substring 'be,'")
# else:
#     print("Doesn't contain substring")

# Replace

c = 'Python is Great'
c1 = 'Annoconda'

c = c.replace('Python', c1)
# print(c)
# new_c = c.replace('Python', c1)
# print(new_c)

# Capatilize the first letter

# d = 'apple'
# d1 = 'APPLE'
# print(d.capitalize())
# print('Even if the string is all in caps, it will lowercaps ever letter and print 1st letter into caps-', d1.capitalize())


# Capatalize every letter
# print(d.upper())

# Lower caps all the letters
# print(d.lower())

# split breaks up a string and returns as list
# Example 1: How split() works in Python?

sp = 'How are you doing?'
# print(sp.split())
# print(sp.split())
# # splits at ','
# print(sp.split(', '))
# # splits at ':'
# print(sp.split(':'))

# Example 2: How split() works when maxsplit is specified?
# Notice the 'TEXT' on maxsplit on index '0' till index of the end
# the last value under >> (grocery.split(', ', 5)) which is 5 is stopped till value of 4

grocery = 'Milk, Chicken, Bread, Butter, Cheese, Mango, Grapes'

# maxsplit: 0
# print(grocery.split(', ', 0))
#
# # maxsplit: 1
# print(grocery.split(', ', 1))
#
# # maxsplit: 2
# print(grocery.split(', ', 2))
#
#
# # maxsplit: 5
# print(grocery.split(', ', 5))

# COUNT >>>>>>>>>>> string.count(substring, start=..., end=...)
# Example 1: Count number of occurrences of a given substring

# define string
# string = "if Jeena is there and if Hena brings whats told, I will decide if is should give them or not. if i see any more people."
#  Marker ^                     ^                                        ^                              ^
# substring = "if"

# count = string.count(substring)

# print count - and you will receive the number of times the string inside the variable (SUBSTRING) is present.
# print("The count is:", count)

# Example 2: Count number of occurrences of a given substring using start and end
# string.count(substring, start=..., end=...)
# define string
# string_20 = "Python is awesome, isn't it?"
#  index>>>  0123456789012345678901234567
# substring = "i"

# count after first 'i' and before the last 'i'
count_z = string_20.count(substring, 8, 25)
# print(len(string_20))
# print(string_20.index('isn'))
# print(index(string))


# print count
# print("The count is:", count_z)


# ALL STRING METHODS - Website on top

# Python String capitalize()
# Python String center()
# Python String casefold()
# Python String count()
# Python String endswith()
# Python String expandtabs()
# Python String encode()
# Python String find()
# Python String format()
# Python String index()
# Python String isalnum()
# Python String isalpha()
# Python String isdecimal()
# Python String isdigit()
# Python String isidentifier()
# Python String islower()
# Python String isnumeric()
# Python String isprintable()
# Python String isspace()
# Python String istitle()
# Python String isupper()
# Python String join()
# Python String ljust()
# Python String rjust()
# Python String lower()
# Python String upper()
# Python String swapcase()
# Python String lstrip()
# Python String rstrip()
# Python String strip()
# Python String partition()
# Python String maketrans()
# Python String rpartition()
# Python String translate()
# Python String replace()
# Python String rfind()
# Python String rindex()
# Python String split()
# Python String rsplit()
# Python String splitlines()
# Python String startswith()
# Python String title()
# Python String zfill()
# Python String format_map()