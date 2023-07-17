import pandas as pd

print(pd.__version__)
# 2.0.3

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
#     cars  passings
# 0    BMW         3
# 1  Volvo         7
# 2   Ford         2

'''--------------------------------------------------------------'''
'''--------------------    Pandas Series   ----------------------'''
'''--------------------------------------------------------------'''
# Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

a = [1,7,2]

myser = pd.Series(a)
print(myser)

# 0    1
# 1    7
# 2    2
# dtype: int64

'''  Labels '''
# If nothing else is specified, the values are labeled with their
#  index number. First value has index 0, second value has index 1
#  etc.

#Return the first value of the Series
print(myser[0])
# 1


''' create labels '''
myser = pd.Series(a, index = ["x","y","z"])
print(myser)
# x    1
# y    7
# z    2
# dtype: int64
print(myser["z"])
# 2


''' Key/Value Objects as Series '''

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

mycal = pd.Series(calories)
print(mycal)
# day1    420
# day2    380
# day3    390

mycal = pd.Series(calories, index = ["day1", "day2"])
print(mycal)
# day1    420
# day2    380

# Note: The keys of the dictionary become the labels.



'''--------------------------------------------------------------'''
'''--------------------     DataFrames     ----------------------'''
'''--------------------------------------------------------------'''
# A Pandas DataFrame is a 2 dimensional data structure, like a 2
#  dimensional array, or a table with rows and columns.

data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}

#Create a DataFrame from two Series
mydata = pd.DataFrame(data)
print(mydata)
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45
