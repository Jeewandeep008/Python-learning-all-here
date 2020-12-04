# DICTIONARIES - DIC
# https://www.programiz.com/python-programming/methods/dictionary/pop

# Dictionary for Subjects
student_name = {
    'Name_1' : 'Students Name',
    'Students Name' : 'Jeewan Deep Tete'
}
subjects = {
    'English' : 'en_marks',
    'Hindi' : 'hi_marks',
    'Bengali' : 'ben_marks',
    'Maths' : 'ma_marks',
    'Science' : 'sci_marks',
    'Geography' : 'geo_marks',
    'History_and_Civics' : 'his_civ_marks',
    'Commerce' : 'com_marks',
    'Business_studies' : 'bs_marks',
    'Accounts' : 'ac_marks',
    'Physics' : 'phy_marks',
    'Chemistry' : 'che_marks',
    1: 'English',
    2: 'Hindi',
    3: 'Bengali',
    4: 'Maths',
    5: 'Science',
    6: 'Geography',
    7: 'History_and_Civics',
    8: 'Commerce',
    9: 'Business_studies',
    10: 'Accounts',
    11: 'Physics',
    12: 'Chemistry',
}

def the_print():
    # subjects.update(en_marks)
    subjects.update(English = 61)
    # subjects.update(Hindi = input("Type a numer: "))
    subjects.update(Hindi = 52)
    subjects.update(Bengali = 63)
    subjects.update(Maths = 56)
    subjects.update(Science = 76)
    subjects.update(Geography = 86)
    subjects.update(History_and_Civics = 86)
    subjects.update(Commerce = 96)
    subjects.update(Business_studies = 55)
    subjects.update(Accounts = 75)
    subjects.update(Physics = 44)
    subjects.update(Chemistry = 88)

    print(student_name['Name_1'],':', '-', student_name['Students Name'])
    print('____________________________________')
    print('Subject :',subjects[1], '-', subjects['English'])
    print('Subject :',subjects[2], '-', subjects['Hindi'])
    print('Subject :',subjects[3], '-', subjects['Bengali'])
    print('Subject :',subjects[4], '-', subjects['Maths'])
    print('Subject :',subjects[5], '-', subjects['Science'])
    print('Subject :',subjects[6], '-', subjects['Geography'])
    print('Subject :',subjects[7], '-', subjects['History_and_Civics'])
    print('Subject :',subjects[8], '-', subjects['Commerce'])
    print('Subject :',subjects[9], '-', subjects['Business_studies'])
    print('Subject :',subjects[10], '-', subjects['Accounts'])
    print('Subject :',subjects[11], '-', subjects['Physics'])
    print('Subject :',subjects[12], '-', subjects['Chemistry'])

    print('____________________________________')
# the_print()

# Other

# month_conversions = {
#     'Jan': 'January',
#     'Feb': 'Febuary',
#     'Mar': 'March',
#     'Apr': 'April',
#     'May': 'May',
#     'Jun': 'June',
#     'Jul': 'July',
#     'Aug': 'August',
#     'Sep': 'September',
#     'Oct': 'October',
#     'Nov': 'November',
#     'Dec': 'December',
#     1: 'January',
#     2: 'Febuary',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'July',
#     8: 'August',
#     9: 'September',
#     10: 'October',
#     11: 'November',
#     12: 'December',
# }

# print(month_conversions[1])
# print(month_conversions['Aug' and 'Sep'])
# print(month_conversions['Aug' or 'Sep'])
# print(month_conversions.get('Jun'))
# print(month_conversions.get('Jun' and 'Mar'))
# print(month_conversions.get('Jun' or 'Mar'))
# print(month_conversions.get('Aun'))
# print(month_conversions.get('Aun', 'Not a valid key'))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Python has a set of built-in methods that you can use on dictionaries.
# EG
new_due_dict = {
    'Anna' : '2000',
    'Tarun' : '1000',
    'Jasime' : '1500',
    'Piko' : '1500',
}
# Method	Description
# clear()	Removes all the elements from the dictionary
# eg_clear = new_due_dict.clear()
# print(eg_clear)

# copy()	Returns a copy of the dictionary eg >> new = d1.copy()
# eg_copy = new_due_dict.copy()
# print(eg_copy)

# https://www.programiz.com/python-programming/methods/dictionary/fromkeys
# fromkeys()	Returns a dictionary (from a sequence of keys) the specified keys and value
# Creates a new dictonary by changing the value mentioned by the user
# dictionary.fromkeys(sequence[, value]) / # dictionary.fromkeys(Key/variable, value/variable])
# eg_fromkey = new_due_dict.fromkeys(new_due_dict, 10)
# output = {'Anna': 10, 'Tarun': 10, 'Jasime': 10, 'Piko': 10}
# eg_fromkey = new_due_dict.fromkeys(new_due_dict) # Blank values
# output = {'Anna': None, 'Tarun': None, 'Jasime': None, 'Piko': None}
# v1 = 'Tacco'
# eg_fromkey = new_due_dict.fromkeys(new_due_dict, v1)
# print(eg_fromkey)
# Output = {'Anna': 'Tacco', 'Tarun': 'Tacco', 'Jasime': 'Tacco', 'Piko': 'Tacco'}
# dictionary comprehension >>>>>>>>>>>>>>>>>>>>>> in fromkey()
# vowels = { key : list(value) for key in Original_dic }
# neww = {i : list(str(2)) for i in new_due_dict} #same
# val = [1]
# new_eg_fromkey = {i : list(val) for i in new_due_dict} #same
# print(new_eg_fromkey)
# output = {'Anna': [1], 'Tarun': [1], 'Jasime': [1], 'Piko': [1]}
# val.append(2)
# print(val)
# print(new_eg_fromkey)
# Output = {'Anna': [1], 'Tarun': [1], 'Jasime': [1], 'Piko': [1]}

# get()	Returns the VALUE of the specified key >>>> dict.get(key[, value])
# eg_get = new_due_dict.get('Anna')
# print(eg_get)
# Output = 2000
# eg_get_1 = new_due_dict.get('Pito', 'Mito')
# print(eg_get_1)
# Pito and mito are not there in the dictionary and .get() only fetches if its there
# new_due_dict.get('Pito', 'Mito')
# print(new_due_dict)
# Output = {'Anna': '2000', 'Tarun': '1000', 'Jasime': '1500', 'Piko': '1500'}

# items()	Returns a list containing a tuple for each key value pair
# dictionary.items()
# eg_items = (new_due_dict.items())
# print(eg_items)
# Output = dict_items([('Anna', '2000'), ('Tarun', '1000'), ('Jasime', '1500'), ('Piko', '1500')])

# keys()	Returns a list containing the dictionary's keys
# eg_keys = new_due_dict.keys()
# print(eg_keys)
# Output = dict_keys(['Anna', 'Tarun', 'Jasime', 'Piko'])

# values()	Returns a list of all the values in the dictionary
# eg_values = new_due_dict.values()
# print(eg_values)
# Output = dict_values(['2000', '1000', '1500', '1500'])

# pop()	Removes the element or the specified key
# new_due_dict.pop('Jasime')
# print(new_due_dict)
# Output = {'Anna': '2000', 'Tarun': '1000', 'Piko': '1500'}

# popitem()	Removes the last inserted key-value pair
# The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.
# eg_popitem = new_due_dict.popitem()
# print(eg_popitem)
# Output = ('Piko', '1500')

# setdefault()	Returns the value of the specified key. If the key does
# not exist: insert the key, with the specified value >> dict.setdefault(key[, default_value])
# new_due_dict.setdefault('Jim', 'Lambo')
# print(new_due_dict)
# Output = {'Anna': '2000', 'Tarun': '1000', 'Jasime': '1500', 'Piko': '1500', 'Jim': 'Lambo'}
# eg_setdefault = new_due_dict.setdefault('Jim', 'Lambo')

# update()	Updates the dictionary with the specified key-value pairs
# Already provided in the 3 ways to update..>>>>>>>>>>>> Check

# del a key from the dictionary
# del [dictionary_name[key_name]]
# del[new_due_dict['Tarun']]
# print(new_due_dict)
# Output = {'Anna': '2000', 'Jasime': '1500', 'Piko': '1500'}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Python Dictionary values()
# The values() method returns a view object that displays a
# list of all the values in the dictionary.
#  >>>>>
# Python Dictionary update()
# The update() method updates the dictionary with the
# elements from the another dictionary object or from
# an iterable of key/value pairs.
# update() method adds element(s) to the dictionary
# if the key is not in the dictionary it updates the key with the new value.
#  >>>>>
# Python Dictionary pop() >>> dictionary.pop(key[, default])
# The pop() method removes and returns an element from a dictionary having the given key.
# Example 1: Pop an element from the dictionary
# # random sales dictionary
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
#
# element = sales.pop('apple')
# print('The popped element is:', element)
# print('The dictionary is:', sales)
# Output
#
# The popped element is: 2
# The dictionary is: {'orange': 3, 'grapes': 4}
#  >>>>>

# Python dictionary_name = dict(zip(Key_variable, value_variable)

# print(new_dic)

# Output
# {1: 'Vanila', 2: 'Kulfi', 3: 'Stawbary', 4: 'Choco'}

# UPDATE METHOD - 3
# ADD value to dictionary
# def add_new_dic():
#     new_dic[5] = 'Mango'
#     new_dic[1] = 'Blackberry'
#     new_dic[6] = 50
    # Other way to add or upate is
    # new_dic.update(2 = 100, 3 = 500, 4 = 1000) or
    # d = {2 = '100', 3 = '500', 4 = '1000'}
    # new_dic.update(d)
    # print(new_dic)

# SET
# key = {1, 2, 3, 4}
# value = {'Choco', 'Vanila', 'Stawbary', 'Kulfi'}
# print(type(value))
# new_dic = dict(zip(key, value))
# print(new_dic)
# add_new_dic()

# 2 datas in the same KEY
# puting a list inside a key of a dictionary as a value
# doma = {1 : ['Hola','Bhola']}
# print(doma)

# Put a dictionary under a key of a dictionary as a value
kito = {2 : {'Maruti', 'Toyota'}}
# print(type(kito))
# print(kito)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  3 ways to update DICTIONARY

# dictionary = {
#     '1' : 'One',
#     '2' : 'Two',
#     '4' : 'Four',
#     '5' : 'Five',
#     '6' : 'Six',
#     '7' : 'Seven',
#     '8' : 'Eight',
# }

# update first method
# Best way to update for KEY HAVING '1' AS '1' : 'Two'
# x = {'1' : 'Twenty'}
# dictionary.update(x)
# print(dictionary)

# 2nd way to update
# not working for key with >> '1' : 'two'
# dictionary.update(one = 'two')
# dictionary.update(1 = 'two') >> does not work
# print(dictionary)

# 3rd way to update

# dictionary['1'] = 100
# dictionary['10'] = 100
# dictionary['9'] = 100
# print(dictionary)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Nested dictionary
people = {1:
              {'name': 'John',
               'age': '27',
               'sex': 'Male'},
          2:
              {'name': 'Marie',
               'age': '22',
               'sex': 'Female'}
          }

# print(people[1])
# print(people[1]['name'])
# print(people[1]['sex'])

# to add a new line
people[3] = {'name': 'Jim',
          'age': '40',
          'sex': 'Male'
          }
# print(people)

# Iterating Through a Nested Dictionary