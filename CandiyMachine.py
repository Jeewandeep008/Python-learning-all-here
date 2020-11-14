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