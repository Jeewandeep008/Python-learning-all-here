# Read files here

# file = open('read_file_example.txt', 'r')
# open('read_file_example.txt', 'r+')
# open('read_file_example.txt', 'w')
# open('read_file_example.txt', 'a')
# returns a boolean value depending upon - open('read_file_example.txt', 'r') <<< 'r'
# print(file.readable())
# shows all info in the file
# print(file.read())
# reads first line and if print again reads second line >>> 1 at a time
# print(file.readline())
# prints all in a list
# print(file.readlines())

# read with for loop >> prints each lines of the file
# for all_files_data in file.readlines():
#     print(all_files_data)
# file.close()

# Append
new_file = open('read_file_example.txt', 'a')
# new_file.write('1. Wake up early in the morning.')
# Into a new line >>>> \n are escape characters
# new_file.write('\n2. Brush your teeth properly.')
# new_file.write('\n3. No abuse.')

# new_file = open('read_file_example.txt', 'w')