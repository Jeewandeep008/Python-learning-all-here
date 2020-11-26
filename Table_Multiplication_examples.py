dictionary = {
    '1' : 'One',
    '2' : 'Two',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
}


dictionary[9] = ['soda', 'loli']
# print(dictionary)

zx = {
    1 : {'we', 'are', 'great'},
    2 : {'we', 'are', 'great'}
}

# print(zx)
# print(type(zx))

# TABLE for a single number
def table_1():
    val = 9
    for i in range(1,11):
        cal = val * i
        print(val, 'x', i , '=', cal)
# table_1()
# Output_1 =
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90

# Table for multiple numeber
def table_2():
    base_val = range(1,13)
    sc_num = range(1,11)
    table_title = 1

    for fst_c in base_val:
        print('_____''Table of - ', table_title,'_____')
        table_title += 1
        for scnd_c in sc_num:
            cal = fst_c * scnd_c
            print(fst_c, 'x' , scnd_c, '=', cal)
    else:
        print('_____________________________')
# table_2()