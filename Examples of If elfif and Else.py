# IF Else elseif or elif

def tester(name):
    baby = 'baby'
    child = 'child'
    teenager = 'teenager'
    male = 'male'
    female = 'female'
    married = 'married'
    single = 'single'
    # child = True
    # teenager = True
    # male = True
    # female = True
    # married = True
    # single = True
    gender = input('What is your gender: ')
    gender = gender.lower()
    # # type_of = type(gender)
    # # print(type_of)

    if gender == male:
        print('You are a male.')
    elif gender == female:
        print('You are a female.')
    elif gender == baby:
        print('You are a baby. Really !!')
    elif gender == teenager:
        print('You are a teenager.')
    elif gender == child:
        print('You are still a child.')
    elif gender == married:
        print('You are a married.')
    elif gender == single:
        print('You are a single.')
    else:
        print('Error: Wrong informaion provided.')

# print(tester(input('Type your name: ')))
# print(tester('Jeewan'))