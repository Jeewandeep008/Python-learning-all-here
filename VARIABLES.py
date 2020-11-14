# Global variable is this
a = 10
b = 50
print('ID of global a', id(a))
print('ID of global b', id(b))

# calling local variable
def local():
    a = 20
    b = 100

    print('Local variable', a)
# local()

# print('Global variable', a)

# CAllING LOCAL VARIABLE but called Global variable
def local_2():

    b = 100

    print('Funcation calling Local variable, which is absent in the local_2 (F) hence called Global variable -', a)
# local_2()

# CALLING Global variable even when local variable is still present inside the function
def local_3():
    x = globals()['a']
    a = 20
    b = 30
    #  global()['a'] = 500 << Change or update Global 'a' value
    print('ID of local b', id(b))
    print('ID of same global a calling from local_3 function', id(x))
    print('Global/Outside variable of a', x)
local_3()
# To change a global varibale value inside a function use - global()['the_value'] = 50 or 100 or 200
# This is how we call a global variable inside a local function as shown on local_3