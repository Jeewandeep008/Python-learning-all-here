# LOOPS >>>>>>>>>>>>>>>>>>>>>>>>> FOR / while
#  FOR LOOP >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
def exm_1():
    name_10 = 'Python'
    print(name_10)
    print(len(name_10))
    print(list(name_10))

    # # in for loop part 1
    # (For each item in sequence:
    # Execute the body of the loop)
    for ii in name_10:
        print(ii)
# exm_1()

def exm_2():
    dif_lang = ['English', 'Bengali', 'Hindi', 'others']
    print(dif_lang)
    print(dif_lang[0: ])
    print(dif_lang[0: 1])
    print(dif_lang[2: 3])
    # print(dif_lang{})
    print(dif_lang.index('Hindi'))
    print(len(dif_lang))
    # for each lang in the dif_lang list, store that inside lang and print it
    for lang in dif_lang:
#       iterate
        print(lang)
# exm_2()

# Table of multiplication with incrementation
def multiplcation():
    user_inpute = 1
    # user_inpute = int(input('Type your number to get x till 10: '))
    for count in range(1,11): # Keeps running till it reaches the 'END' no. in the range
        output = user_inpute * count
        print(user_inpute, 'x', count, '=', output)
        user_inpute += 1
    else:
        print('_________________________')
        #OR
        # print(user_inpute, 'x', count, '=', user_inpute*count, end='\t')
        # print(user_inpute, 'x', count, '=', user_inpute*count)
# multiplcation()

# With no incrementation
def multiplcation_1():
    user_inpute = 9
    # user_inpute = int(input('Type your number to get x till 10: '))
    print('__________', 'Table -', user_inpute, '__________')
    for count in range(1,11): # Keeps running till it reaches the 'END' no. in the range
        output = user_inpute * count # output = 9 * 1/2/3/4 etc
        print(user_inpute, 'x', count, '=', output)
    else:
        print('_______________________________')
        #OR
        # print(user_inpute, 'x', count, '=', user_inpute*count, end='\t')
        # print(user_inpute, 'x', count, '=', user_inpute*count)
# multiplcation_1()

# Tried multiplication table from 1 to 12
def multiplcation_2():
    # for each count in the range, store that inside count and print it or do the following
    for count in range(1,13): # Keeps running till it reaches the 'END' no. in the range
        print('__________','Table -',count,'__________')
        print(count)
        for count_2 in range(1,11): # condition till 1 to 10
            output = count_2 * count # output = 1*1 = 1 then print /next  2*1 = 2 till 10*1 = 10
            print(count_2, 'x', count, '=', output)

    else:
        print('________________________________')
        print('End of the Table')
# multiplcation_2()

# Note : for count in range(1,13): >> Has its outer condition for start no.:1 till End no.: 12
# Now the 'COUNT' has the value 1 eg : count = 1
# The second (for count_2 in range(1,11):) as a inner condition which 1st needs to be shorted out.
# Now the 'COUNT_2' has value count_2 = 1
# Hence, count_2 range(1,11) is printed continuing with the count = 1 value remaining constant till it reaches range 10 leaving 11
# As soon as it reaches 10 the condition is over and then the function is run again from top with the next range from count.
# And so on.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>

# iteration
# condition
# Compilation
# Execute
# indentation
#
