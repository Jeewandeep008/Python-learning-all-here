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

# MOD CALCULATOR

# def mod_mod(num1, num2):
#     value = round(float(num1) % float(num2))
#     # value = float(num1) % float(num2)
#     print(value)

# mod_mod(input('Type your first value: '), input('Type your second value: '))


# Calculator
import operator

# If else statements
# def cal():
#
#     user_fir_num = float(input('Type your num: '))
#     choice = input('Choose from ( +,-,/,**,*,(),%, = ) : ')
#     user_sec_num = float(input('Type your num: '))
#
#     if choice == '+':
#         print(user_fir_num, '+', user_sec_num,'\n', '=', user_fir_num + user_sec_num)
#
#     elif choice == '-':
#         print(user_fir_num, '-', user_sec_num,'\n', '=', user_fir_num - user_sec_num)
#
#     elif choice == '*':
#         print(user_fir_num, '*', user_sec_num,'\n', '=', user_fir_num * user_sec_num)
#
#     elif choice == '/':
#         print(user_fir_num, '/', user_sec_num,'\n', '=', user_fir_num / user_sec_num)
#
#     elif choice == '**':
#         print(user_fir_num, 'pow**', user_sec_num,'\n', '=', user_fir_num ** user_sec_num)
#
#     elif choice == '%':
#         print(user_fir_num, '%', user_sec_num,'\n', '=', user_fir_num % user_sec_num)
#
#     else:
#         print('Invalid error.')
#
# # cal()
#
# # Works infinate times unless pressed enter to exit
# # works part by part not continuous
# def cal1():
#     try:
#         new_value = 0
#         operators_list = ['()', '/', '*', '+', '-', '=' ]
#
#         while True:
#             new_value = new_value
#             user_fir_num = float(input('Type your num: '))
#             choice = input('Choose from ( +,-,/,**,*,(),%, = ) : ')
#             user_sec_num = float(input('Type your num: '))
#             # result = user_fir_num, choice , user_sec_num
#             # print(result)
#
#             if choice == '':
#                 return
#
#             elif choice == '+':
#                 var_add = user_fir_num + user_sec_num
#                 new_value += var_add
#                 print(user_fir_num, '+', user_sec_num,'\n', '=', var_add)
#
#             elif choice == '-':
#                 var_sub = user_fir_num - user_sec_num
#                 new_value -= var_sub
#                 print(user_fir_num, '-', user_sec_num,'\n', '=', var_sub)
#
#             elif choice == '*':
#                 var_multi = user_fir_num * user_sec_num
#                 new_value *= var_multi
#                 print(user_fir_num, '*', user_sec_num,'\n', '=', var_multi)
#
#             elif choice == '/':
#                 var_div = user_fir_num / user_sec_num
#                 new_value /= var_div
#                 print(user_fir_num, '/', user_sec_num,'\n', '=', var_div)
#
#             elif choice == '**':
#                 var_pow = user_fir_num ** user_sec_num
#                 new_value **= var_pow
#                 print(user_fir_num, 'pow**', user_sec_num,'\n', '=', var_pow)
#
#             elif choice == '%':
#                 var_module = user_fir_num + user_sec_num
#                 new_value %= var_module
#                 print(user_fir_num, '%', user_sec_num,'\n', '=', var_module)
#
#             else:
#                 print('Invalid error.')
#
#     except ValueError:
#         print('''Invalid Error.','\n',
#         'You have either skipped a value or symbol or entered a wrong input.''','''\n''',
#               '''Please try again.''')
#
# # cal1()




# Main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FINAL >>>>>>>>>>>>>>>>>>>>>>>>>>>
# def cal2():
#     try:
#         dictionary_operator = {
#             '+' : operator.add,
#             '-' : operator.sub,
#             '/' : operator.truediv,
#             '*' : operator.mul,
#             '%' : operator.mod,
#             '^' : operator.xor,
#             '**' : operator.pow,
#             '=' : operator.eq,
#         }
#
#         while True:
#             output_1 = 0
#             count = 0
#             user_fir_num = float(input('Type your 1st num or hit enter to exit: '))
#             choice = input('Choose from +,-,/,**,*,(),%,= : ')
#             user_sec_num = float(input('Type your 2nd num or hit enter to exit: '))
#             choice_1 = input('Choose from +,-,/,**,*,(),%,= : ')
#             # result = user_fir_num, choice , user_sec_num
#             # print(result)
#
#             if choice == '=':
#                 return
#
#
#             # 01
#             elif choice_1 == '=' and count == 0:
#                 new_val = dictionary_operator.get(choice)
#                 # eg: (operator.add(5,5))
#                 output = new_val(user_fir_num, user_sec_num)
#                 print('=', output)
#                 return
#
#             # 02
#             elif choice in dictionary_operator and count == 0:
#                 new_val = dictionary_operator.get(choice)
#                 # eg: (operator.add(5,5))
#                 output = new_val(user_fir_num, user_sec_num)
#                 print('=', output)
#
#                 user_third_num = float(input('Type your 3rd num or hit enter to exit: '))
#
#                 new_val = dictionary_operator.get(choice_1)
#                 output = new_val(output, user_third_num)
#                 print('=', output)
#
#                 choice_2 = input('Choose from +,-,/,**,*,(),%,= : ')
#
#                 output_1 = output
#                 print('Output_1 = ', output_1)
#                 count += 1
#                 print('Count = ', count)
#                 # **********************************************
#                 user_fir_num = float(input('Type your 1st num or hit enter to exit: '))
#
#                 new_val = dictionary_operator.get(choice_2)
#                 output = new_val(output_1, user_fir_num)
#                 print('=', output)
#                 if choice == '=':
#                     return
#
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 user_sec_num = float(input('Type your 2nd num or hit enter to exit: '))
#                 # choice_1 = input('Choose from +,-,/,**,*,(),%,= : ')
#
#                 new_val = dictionary_operator.get(choice)
#                 output = new_val(output, user_sec_num)
#                 print('=', output)
#
#                 output_1 = output
#                 print('Output_1 = ', output_1)
#                 count += 1
#                 print('Count = ', count)
#                 return
#
#
#             else:
#                 print('Invalid error.')
#
#     except ValueError:
#         print('Sucessfully exit.')
#         # print('''Invalid Error.','\n',
#         # 'You have either skipped a value or symbol or entered a wrong input.''','''\n''',
#         #       '''Please try again.''')
#
# # cal2()


# Main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FINAL >>>>>>>>>>>>>>>>>>>>>>>>>>>
# try:
#
#     def cal3(user_fir_num, choice, user_sec_num):
#         try:
#             dictionary_operator = {
#                 '+': operator.add,
#                 '-': operator.sub,
#                 '/': operator.truediv,
#                 '*': operator.mul,
#                 '%': operator.mod,
#                 '^': operator.xor,
#                 '**': operator.pow,
#                 '=': exit
#             }
#
#             output_1 = 0
#             count = 0
#             user_fir_num = user_fir_num
#             choice = choice
#             user_sec_num = user_sec_num
#             main = '='
#             # **************************************
#             new_val = dictionary_operator.get(choice)
#             output = new_val(user_fir_num,user_sec_num)
#             # **************************************
#
#             choice_1 = input('To end use = or to continue hit ENTER: ')
#             print('=', output)
#
#             if choice_1 == main:
#                 return
#
#             count += 1
#             print('Count : ', count,'- Continue')
#
#             while choice != main:
#                 output_1 = output
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 # ***********************************
#                 while choice not in dictionary_operator:
#                     choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                     # ***********************************
#                 if choice == main:
#                     return
#
#                 user_fir_num = float(input('Type your 1st num or hit enter to exit: '))
#                 new_val = dictionary_operator.get(choice)
#                 output = new_val(output_1, user_fir_num)
#
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 if choice == main:
#                     print('=', output)
#                     return
#
#                 print('=', output)
#                 output_1 = output
#                 count += 1
#                 print('Count : ', count,'- Continue')
#
#
#                 user_sec_num = float(input('Type your 2nd num or hit enter to exit: '))
#                 new_val = dictionary_operator.get(choice)
#                 output = new_val(output_1,user_sec_num)
#
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 if choice == main:
#                     print('=', output)
#                     return
#
#                 print('=', output)
#                 output_1 += output
#
#                 count += 1
#                 print('Count : ', count,'- Continue')
#
#             else:
#                 print('=', output_1)
#
#         except ValueError:
#             print('Sucessfully exit.')
            # print('''Invalid Error.','\n',
            # 'You have either skipped a value or symbol or entered a wrong input.''','''\n''',
            #       '''Please try again.''')

#
#     cal3(float(input('Type your 1st num or hit enter to exit: ')), input('Choose from +,-,/,**,*,(),%,= : '), float(input('Type your 2nd num or hit enter to exit: ')))
#
# except ValueError:
#     print('Sucessfully exit.')

# num = (i for i in range(100000000000000000000))
#     while user_fir_num not in num:
#         user_fir_num = float(input('Type your 1st num or hit enter to exit: '))
#     while choice not in dictionary_operator:
#         choice = input('Choose from +,-,/,**,*,(),%,= : ')
#     while user_sec_num not in num:
#         user_fir_num = float(input('Type your 2st num or hit enter to exit: '))

# Main >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Full and FINAL >>>>>>>>>>>>>>>>>>>>>>>>>>>

# try:
#
#     def cal3(user_fir_num, choice, user_sec_num):
#         try:
#             dictionary_operator = {
#                 '+': operator.add,
#                 '-': operator.sub,
#                 '/': operator.truediv,
#                 '*': operator.mul,
#                 '%': operator.mod,
#                 # '^': operator.xor,
#                 '**': operator.pow,
#                 '=': exit
#             }
#
#             output_1 = 0
#             count = 0
#             user_fir_num = user_fir_num
#             choice = choice
#             user_sec_num = user_sec_num
#             main = '='
#             # **************************************
#             new_val = dictionary_operator.get(choice)
#             output = new_val(user_fir_num,user_sec_num)
#             # **************************************
#
#             choice = input('Choose from +,-,/,**,*,(),%,= : ')
#             while choice not in dictionary_operator:
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#             if choice == main:
#                 print('Final Ans =', output)
#                 return
#
#             print('Ans =', output)
#             count += 1
#             print('Count : ', count,'- Continue')
#
#             # Loop Start
#             while choice != main:
#                 output_1 = output
#
#                 # 1st number
#                 user_fir_num = float(input('Type your 1st num or hit enter to exit: '))
#
#                 new_val = dictionary_operator.get(choice)
#                 output = new_val(output_1, user_fir_num)
#
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 while choice not in dictionary_operator:
#                     choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 if choice == main:
#                     print('Final Ans =', output)
#                     return
#
#                 print('Ans =', output)
#                 output_1 = output
#                 count += 1
#                 print('Count : ', count,'- Continue')
#
#                 # 2nd number
#                 user_sec_num = float(input('Type your 2nd num or hit enter to exit: '))
#
#                 new_val = dictionary_operator.get(choice)
#                 output = new_val(output_1,user_sec_num)
#
#                 choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 while choice not in dictionary_operator:
#                     choice = input('Choose from +,-,/,**,*,(),%,= : ')
#                 if choice == main:
#                     print('Final Ans =', output)
#                     return
#
#                 print('Ans =', output)
#                 output_1 = output
#
#                 count += 1
#                 print('Count : ', count,'- Continue')
#
#             # else:
#             #     print('=', output_1)
#
#         except ValueError:
#             print('Final output =', output_1)
#             print('Sucessfully exit.')
#
#     cal3(float(input('Type your 1st num or hit enter to exit: ')), input('Choose from +,-,/,**,*,(),%,= : '), float(input('Type your 2nd num or hit enter to exit: ')))
#
# except ValueError:
#     print('Sucessfully exit.')


# SOME CHANGE
try:

    def cal3(user_fir_num, choice, user_sec_num):
        try:
            dictionary_operator = {
                '+': operator.add,
                '-': operator.sub,
                '/': operator.truediv,
                '*': operator.mul,
                '%': operator.mod,
                # '^': operator.xor,
                '**': operator.pow,
                '=': exit,
                'c' : exit,
            }

            output_1 = 0
            count = 0
            user_fir_num = user_fir_num
            choice = choice
            user_sec_num = user_sec_num
            main = 'c'
            # **************************************
            new_val = dictionary_operator.get(choice)
            output = new_val(user_fir_num, user_sec_num)
            # **************************************
            print('Ans =', output)

            choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')
            while choice not in dictionary_operator:
                choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')

            while choice == '=':
                print('Ans =', output)
                choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')
            if choice == main:
                print('Final Ans =', output)
                return

            count += 1
            print('Count : ', count, '- Continue')

            # Loop Start
            while choice != main:
                output_1 = output

                # 1st number
                user_fir_num = float(input('Type your 1st num or hit enter to exit: '))

                new_val = dictionary_operator.get(choice)
                output = new_val(output_1, user_fir_num)
                print('Ans =', output)

                choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')
                while choice not in dictionary_operator:
                    choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')

                while choice == '=':
                    print('Ans =', output)
                    choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')
                if choice == main:
                    print('Final Ans =', output)
                    return

                output_1 = output
                count += 1
                print('Count : ', count, '- Continue')

                # 2nd number
                user_sec_num = float(input('Type your 2nd num or hit enter to exit: '))

                new_val = dictionary_operator.get(choice)
                output = new_val(output_1, user_sec_num)
                print('Ans =', output)

                choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')
                while choice not in dictionary_operator:
                    choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')

                while choice == '=':
                    print('Ans =', output)
                    choice = input('Choose from +,-,/,**,*,(),%,=,c to exit : ')
                if choice == main:
                    print('Final Ans =', output)
                    return

                output_1 = output
                count += 1
                print('Count : ', count, '- Continue')

            # else:
            #     print('=', output_1)

        except ValueError:
            print('Final output =', output_1)
            print('Sucessfully exit.')


#     cal3(float(input('Type your 1st num or hit enter to exit: ')),
#          input('Choose from +,-,/,**,*,(),%,= : '),
#          float(input('Type your 2nd num or hit enter to exit: ')))
#
# except ValueError:
#     print('Sucessfully exit.')