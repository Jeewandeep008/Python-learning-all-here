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
# print(subjects)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# en_marks = {'Target or Key': 'new value'} # To Update
# en_marks = {'English': '60'}
# hi_marks = {'Hindi': '55'}
# ben_marks = {'Bengali': '63'}
# ma_marks = {'Maths': '75'}
# sci_marks = {'Science': '90'}
# geo_marks = {'Geography': '55'}
# his_civ_marks = {'History_and_Civics': '75'}
# com_marks = {'Commerce': '80'}
# bs_marks = {'Business_studies': '85'}
# ac_marks = {'Accounts': '52'}
# phy_marks = {'Physics': '63'}
# che_marks = {'Chemistry': '52'}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# The Updates
# d = {'x': 2} < X is the key and needs to be in the said dictionary
# d.update(y = 3, z = 0) <<< Other way of updating
def the_print():
    # subjects.update(en_marks)
    subjects.update(English = 60)
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
    total = subjects[
        'English' and
        'Hindi' and
        'Bengali' and
        'Maths' and
        'Science' and
        'Geography' and
        'History_and_Civics' and
        'Commerce' and
        'Business_studies' and
        'Accounts' and
        'Physics' and
        'Chemistry'
    ]

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
    print(total)
    print('____________________________________')
# the_print()
# UPDATE METHOD - 1
# Example 1: Working of update()
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}

# # updates the value of key 2
# d.update(d1)
# print(d)

# d1 = {3: "three"}
#
# # adds element with key 3
# d.update(d1)
# print(d)
# UPDATE METHOD - 2
# Example 2: update() When Tuple is Passed
# d = {'x': 2}

# d.update(y = 3, z = 0)
# print(d)

# Output
# {'x': 2, 'y': 3, 'z': 0}


# Python has a set of built-in methods that you can use on dictionaries.
#
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

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

# Example 1: Working of update()
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}

# updates the value of key 2
# d.update(d1)
# print(d)

# d1 = {3: "three"}

# adds element with key 3
# d.update(d1)
# print(d)

# Python Dictionary values()
# The values() method returns a view object that displays a
# list of all the values in the dictionary.
#  >>>>>
# Python Dictionary update()
# The update() method updates the dictionary with the
# elements from the another dictionary object or from
# an iterable of key/value pairs.
# update() method adds element(s) to the dictionary
# if the key is not in the dictionary. If the key is
# in the dictionary, it updates the key with the new value.
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

key = {1,2,3,4}
value = {'Choco','Vanila','Stawbary','Kulfi'}

new_dic = dict(zip(key,value))
# print(new_dic)

# Output
# {1: 'Vanila', 2: 'Kulfi', 3: 'Stawbary', 4: 'Choco'}

# UPDATE METHOD - 3
# 3 ways to update the data in dictionary
# ADD value to dictionary
def add_new_dic():
    new_dic[5] = 'Mango'
    new_dic[1] = 'Blackberry'
    new_dic[6] = 50
    # Other way to add or upate is
    # new_dic.update(2 = 100, 3 = 500, 4 = 1000) or
    # d = {2 = '100', 3 = '500', 4 = '1000'}
    # new_dic.update(d)
    print(new_dic)
# add_new_dic()

# 2 datas in the same KEY
# puting a list inside a key of a dictionary as a value
# doma = {1 : ['Hola','Bhola']}
# print(doma)

# Put a dictionary under a key of a dictionary as a value
kito = {2 : {'Maruti', 'Toyota'}}
print(type(kito))
print(kito)