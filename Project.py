# webiste - https://code.visualstudio.com/docs/languages/python

# v6 = 'Strings'
# print(v6)



# s1 = 'Jeewan' 'Deep' 'Tete'
# print(s1)

# n1 = 'Jeewan'
# age1 = '26'
# address1 = 'Selimpur'
# city1 = 'Kolkata'
# gender1 = True;
# print('Hi! My name is ' + n1 + ' and I am ' + age1 + ' years old.' + ' I live in ' + address1 + ' area and i am looking for work in '+ city1 + ' city.')

# uppercase and lower case and true or false
# v7 = 'Python Is Great'
# print(v7.lower())
# print(v7.upper())
# print(v7.isupper())
# print(v7.islower())
# print(v7.upper().isupper())
# print(v7.lower().islower())
# print(len(v7))
# print(v7[0])
# print(v7.index('I'))

#  REPLACE

# print(v7.replace('Python', 'Annoconda'))
# print(v7)

# change a number into a string to print the string along with the number

# num_1 = 100
# print(str(num_1) + ' is my fav number.')

# >>>> INPUTE - asking user to type a name or number

# char_name = input('What is your name: ')
# char_age = input('What is your age: ')
# print('Hi ' + char_name + '. Your age is ' + char_age + '.')

# CHNAGING AN INPUTE VALUE WHICH IS ACTUALLY A STRING NOW TO A NUMBER
# CHANGE IT INTO NUMBER BY >>> INIT / FLOAT / FLOOR

# val_1 = input('Type your first number value: ')
# val_2 = input('Type your second number value: ')

# result0 = float(val_1) + float(val_2)
# print(floor(result0))
# print(result0)


# FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def sayhi():
#     print('Hello')

# sayhi()

# def school(sch):
#     user_name = input('Whats your name?:')
#     print('Hello ' + user_name + '. Your school same is: ' + sch + '.')

# school(input('Type your school name: '))

# def gm(user, game):
#     print('Hi ' + user + '. Your fav game is ' + game + '.')

# # gm(input('What is your name: ' and 'Your fav game:'))
# gm(input('What is your name:'), input('Your fav game:'))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Binary calculator Part 1 - bmi
#  WORKING PERFECTLY

# def calculation(val_1, operator, val_2):
    
#     if operator == '+':
#         # operator.add()
#         print('Add = ', float(val_1) + float(val_2))
#     elif operator == '-':
#         # operator.sub()
#         print('Sub = ', float(val_1) - float(val_2))
#     elif operator == '*':
#         # operator.mul()
#         print('Mul = ', float(val_1) * float(val_2))
#     elif operator == '/':
#         # operator.div()
#         print('Div = ', float(val_1) / float(val_2))
#     elif operator == '**':
#         # operator.pow()
#         print('Power off = ', float(val_1) ** float(val_2))
#     elif operator == '%':
#         # operator.mod()
#         print('Mode = ', val_1 % val_2)
#     else:
#         print('Error: Invalid Details Provided. Try again.')

# calculation(input('Type your first number: '), input('Type eg: +,- etc: '), input('Type your second number: '))

# def calci(num_1, operator, num_2):
#     if operator == '+'or operator == '-' or operator == '*' or operator == '/' or operator == '**' or operator == '%':
#         print('Add = ', float(num_1) + float(num_2))
#         print('Sub = ', float(num_1) - float(num_2))
#         print('Mul = ', float(num_1) * float(num_2))
#         print('Div = ', float(num_1) / float(num_2))
#         print('Power off = ', float(num_1) ** float(num_2))
#         print('Mod = ', float(num_1) % float(num_2))
#         print('Absolute/ADD = ', abs(float(num_1) + float(num_2)))
#         print('Round_up/ADD = ', round(float(num_1) + float(num_2)))
#     else:
#         print('Error: Invalid Details Provided. Try again.')

# calci(input('Type your first number: '), input('Type eg: +,- etc: '), input('Type your second number: '))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Others
# ran_1 = 4
# #  max - among these numbers which one is higher
# print(max(ran_1, 100))
# #  min - among these numbers which one is min
# print(min(ran_1, 1))
# #  ROUND number
# print(round(3.4))
# print(round(3.5))
# print(round(3.8))

# floor
# print(floor(3.7))
# print('This is a floor() example.')
# print('Square root of >')
# print(sqrt(10))
# print(sqrt(5))

# nn = jam
# print(nn)
# NameError: name 'jam' is not defined

# nn_n = 'Jam'
# print(nn_n)

# nam = 2
# nam_1 = '2'
# print(nam)
# print(nam_1)

# FUNCTION with return  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def cube(num, num1):
#     return num**num1

# print(cube(5,2))
# print(cube(5,5))
# print(cube(5,10))

# Remove all the odd and even numbers from list / RANGE >>>>>>>>>>>>>>>>>>
# rem_odd = [1,3,5,7,9,2,4,6,8,10]
# rem_even = [1,3,5,7,9,2,4,6,8,10]
# L = range(10)
# for a in L:
# print(a)

# >>>>>>>>>>>>>>>>>>>>>>>> RANGE with list >>>>>>>>>>>>>>>>>>>>>>>> short demo
# nuum = range(10)
# for a in nuum:
# print(a)

# part 1 
# nuum01 = range(11)
# print(nuum01)

# # to see as in list
# new_nuum01 = list(nuum01)
# print(new_nuum01)

# # remove even numbers eg: nuum_02 = range(START,END,NO. OF TIMES IT SHOULD SKIP)
# 2
# nuum_02 = range(0,11,2)
# print(nuum_02)
# new_nuum_02 = list(nuum_02)
# print(new_nuum_02)
# # 3
# nuum_023 = range(0,11,3)
# print(nuum_02)
# new_nuum_02 = list(nuum_023)
# print(new_nuum_02)

# remove odd numbers eg: nuum_02 = range(START,END,NO. OF TIMES IT SHOULD SKIP)
# def odd_1(val):
#     nuum_02 = range(val)
#     print(nuum_02)
#     new_nuum_02 = list(nuum_02)
#     print(new_nuum_02)
#     for i in new_nuum_02:
#         if (i % 2 != 0):
#             new_nuum_02.remove(i)
#     print(new_nuum_02)

# # odd_1(11)  #[0, 2, 4, 6, 8, 10]

# def odd_2(start,end,skip):
#     nuum_02 = range(start,end,skip)
#     print(nuum_02)
#     new_new = list(nuum_02)
#     print(new_new)

# odd_2(0,11,2)  #[0, 2, 4, 6, 8, 10]

# LOOPS >>>>>>>>>>>>>>>>>>>>>>>>> FOR / while 
#  FOR LOOP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# nana = [1,3,5,7,9,2,4,6,8,10]
# for i in nana:
#     if (i%2!=0):
#         nana.remove(i)
# print(nana)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
# print(x)

# for x in "banana":
#       print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# Candies
def part1():
# if else statements
    machine_counts = 1
    user_wants = input('How many candies do you want : ')
    user_wants = int(user_wants)
    num_of_candies = 80
    if  user_wants > num_of_candies:
        print('You can only buy',num_of_candies, 'Candies from this machine.')

    elif machine_counts <= int(user_wants) and not(num_of_candies):
        print('Candies', machine_counts)
        machine_counts += 1
    elif user_wants < num_of_candies:
        print('You have received', user_wants , 'Candies. And the remaining Candies are',num_of_candies - user_wants,'.')
    else:
        user_wants == num_of_candies
        print('You have received', user_wants , 'Candy.')
        print('The machine is now out of stock')
# print(part1())

# or
# While loop >>>>>>>>>>>>>>> CODE NOT WORKING PROPERLY YET
def part2():
    count = 1
    user = input('Number of chocobar : ')
    user = int(user)
    total_choco = 100
    while user > total_choco and user == total_choco:
        print('You can only buy', total_choco,'chocobars.')

    if count <= user:
        print('You have received', user,'chocobars. Please come again.')
        count += 1
    # elif count < total_choco:
    #     print('You have received', user,'chocobars. Please come again.')
    else:
        user == total_choco
        print('You have received',user,' & the stock is now over.')
# print(part2())
# >>>>
# i = 1# initialization
# while i <= 5: # condition
#   print('HELLO PEOPLE !', i)
#   # incrementation
#   i += 1

# Reverse
# i = 0 # initialization
# while i >= -5: # condition
#   print('HELLO PEOPLE !')
#   i -= 1 # incrementation

# TEST >>> WHen a new while loop is created the new one needs news data like the 
# previous one
# ab = 1

# while ab <= 2:
#     # end='' ends the print statement in one line
#     print('lalala', ab, end='')
#     ab += 1
#     jb = 1
#     while jb <= 2:
#         print('bababa' , jb, end='')
#         jb += 1
#     print()
# ab = 1

# while ab <= 5:
#     # end='' ends the print statement in one line
#     print('lalala', ab, end='')
#     jb = 1
#     while jb <= 4:
#         print('bababa' , jb, end='')
#         jb += 1

#     ab += 1
#     print()
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def mod_mod(num1, num2):
#     value = round(float(num1) % float(num2))
#     # value = float(num1) % float(num2)
#     print(value)

# mod_mod(input('Type your first value: '), input('Type your second value: '))

# IF Else elseif or elif

# def tester(name):
#     baby = 'baby'
#     child = 'child'
#     teenager = 'teenager'
#     male = 'male'
#     female = 'female'
#     married = 'married'
#     single = 'single'
#     # child = True
#     # teenager = True
#     # male = True
#     # female = True
#     # married = True
#     # single = True
#     gender = input('What is your gender: ')
#     gender = gender.lower()
#     # # type_of = type(gender)
#     # # print(type_of)
#
#     if gender == male:
#         print('You are a male.')
#     elif gender == female:
#         print('You are a female.')
#     elif gender == baby:
#         print('You are a baby. Really !!')
#     elif gender == teenager:
#         print('You are a teenager.')
#     elif gender == child:
#         print('You are still a child.')
#     elif gender == married:
#         print('You are a married.')
#     elif gender == single:
#         print('You are a single.')
#     else:
#         print('Error: Wrong informaion provided.')

# print(tester(input('Type your name: ')))
# print(tester('Jeewan'))

# BULLIAN

# name_10 = 'Jeewan'
# male = True
# # male = False
# # female = True
# # female = False
# # tall = True
# tall = False
# # short = True
# # short = False 

# if name_10 is male and tall: # M: T / T : T
#     print(name_10 + '. You are a male and you are tall.')

# elif name_10 is male and not(tall):
#     print(name_10 + '. You are a male and your height is small.')

# elif name_10 is male or tall : # Tall : True / Male : True
#     print(name_10 + '. You are a male or you are tall.')

# else : # Male : True / Tall : False
#     print(name_10 + '. You are female and you are short.')
# M: F / T : F

# DICTIONARIES - DIC

month_conversions = {
    'Jan': 'January',
    'Feb': 'Febuary',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
    1: 'January',
    2: 'Febuary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

# print(month_conversions['Aug'])
# print(month_conversions['Aug' and 'Sep'])
# print(month_conversions['Aug' or 'Sep'])
# print(month_conversions.get('Jun'))
# print(month_conversions.get('Jun' and 'Mar'))
# print(month_conversions.get('Jun' or 'Mar'))
# print(month_conversions.get('Aun'))
# print(month_conversions.get('Aun', 'Not a valid key'))


# GUESS GAME
# def guess_game(s_no):
#     # The secret code will be stored here
#     secret_name = s_no
#     # The answer of the user will be stored here temporarely
#     guess = ""
#     # The number of times the user has guessed from beginning
#     guess_counts = 0
#     # The number of times the user can guess
#     guess_limit = 3
#     # If the user has
#     out_of_guess = False
#
#     while guess != secret_name and not(out_of_guess):
#         if guess_counts < guess_limit:
#             guess = input('What is chocolate made of? : ')
#             guess_counts += 1
#         else:
#             out_of_guess = True
#
#     if out_of_guess:
#         print('You are out of guesses & YOU LOSE !')
#     else:
#         print('You won the GAME !')

# print(guess_game('coco'))

# Some examples of AND / OR / NOT  also Bullians of TRUE / FALSE

# poison = False
# food = True
# get_punched = False
# to_punch = True
# play_outside = True
# play_inside = True
# play_inside_alone = True
# play_alone = False
#
# print(poison and food) # False
# print(poison or food) # True
# print(get_punched or to_punch) #True
# print(get_punched and to_punch) #False
