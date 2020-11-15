# >>>>>>>>>>>>>>>>>>>>>>>> RANGE with list >>>>>>>>>>>>>>>>>>>>>>>> short demo
# Remove all the odd and even numbers from list / RANGE >>>>>>>>>>>>>>>>>>
# rem_odd = [1,3,5,7,9,2,4,6,8,10]
# rem_even = [1,3,5,7,9,2,4,6,8,10]
# L = range(10)
# for a in L:
# print(a)

nuum = range(10)
for a in nuum:
    print(a)


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

# With for loop
def raise_to_pow(base_num, pow):
    result = 1
    for i in range(pow):
        result = result * base_num
    return result
# print(raise_to_pow(2,2))

# The process in here is:
#     for i in range(pow): therefore range is = 0,1,2 leaving 3
#         result = result * base_num
# where at first when the for loop is run:
# 1> result = 1 * 2 = 2
# The second time when the for loop is run:
# 2> result = 2 * 2 = 4
# The third time when the for loop is run:
# 2> result = 4 * 2 = 8
