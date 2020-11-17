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

print(month_conversions[1])
# print(month_conversions['Aug' and 'Sep'])
# print(month_conversions['Aug' or 'Sep'])
# print(month_conversions.get('Jun'))
# print(month_conversions.get('Jun' and 'Mar'))
# print(month_conversions.get('Jun' or 'Mar'))
# print(month_conversions.get('Aun'))
# print(month_conversions.get('Aun', 'Not a valid key'))

# Example 1: Working of update()
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)