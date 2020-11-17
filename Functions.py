
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
# The Print

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

# Example 1: Working of update()
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}
#
# # updates the value of key 2
# d.update(d1)
# print(d)
#
# d1 = {3: "three"}
#
# # adds element with key 3
# d.update(d1)
# print(d)

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