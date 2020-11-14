from math import*
# fetches more math functions

# Beginning
# print('Hello world')
# print('    /|')
# print('   / |')
# print('  /  |')
# print(' /   |')
# print('/____|')

# v1 = 'Arithmetics';
# print(v1)

# print(2 + 3)
# print(9 - 8)
# print(2 * 2)
# print(5 / 2) # float number output


# v2 = 'integer division / floor number'
# print(v2)

# print(5 // 2) # Withour decimal floow output
# print(8 + 9 - 10)
# # 8 + 9 -   #SyntaxError: invalid syntax
# # Follow grammer

# v3 = 'Using Brackets () BODMAS - B - Bracket / O - Open / D - Division / M - multiplication / A - Addition / S - Substraction'
# print(v3)
# print(8 + 2 * 3) # first its multiplies asn then it adds
# print((8 + 2) * 3) # first the Bracket () then the Multiplication following BODMAS

# v4 = 'Power OFF / OR Exponent'
# print(v4)

# print(2*2*2) #(2)4
# print(2**2)

# POWER oFF with FUNCTION / FOR loop

def power_off_1(base_num, pow):
    counts = 1
    for val in range(pow):
        counts = base_num * counts
    return counts
# print(power_off_1(2,2))

# or

counts = 1
for val in range(2):
    counts = 2 * counts
    print(counts)

# v5 = 'Modulers'
# print(v5)

# print(10 / 3)
# print(10 % 3) # the answer will give us the remender
# Others
# ran_1 = 4
# absolute
# print(abs(ran_1))
# #  Power off
# print(pow(ran_1, 2))
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
# print(float(3.7))
# print('This is a float() example.')
# print('Ceil rounds the number no matter what number is after the dot')
# print(ceil(2.2))
# print(ceil(2.5))
# print(ceil(2.8))
# print('Square root of >')
# print(sqrt(10))
# print(sqrt(5))