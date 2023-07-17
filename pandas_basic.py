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


''' Locate Row '''

print(mydata.loc[0]) #Return row 0
# calories    420
# duration     50
# returns a Pandas Series

print(mydata.loc[[0]]) #Return row 0
#    calories  duration
# 0       420        50
# using [], the result is a DataFrame

print(mydata.loc[[0,1]]) #return row 0 and 1
#    calories  duration
# 0       420        50
# 1       380        40


''' Named Indexes '''
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

#       calories  duration
# day1       420        50
# day2       380        40
# day3       390        45


''' Load Files Into a DataFrame '''

df = pd.read_csv('data.csv')
#print(df)
#      Duration  Pulse  Maxpulse  Calories
# 0          60    110       130     409.1
# 1          60    117       145     479.0
# 2          60    103       135     340.0
# 3          45    109       175     282.4
# 4          45    117       148     406.0
# ..        ...    ...       ...       ...

'''--------------------------------------------------------------'''
'''-------------------   Read CSV Files     ---------------------'''
'''--------------------------------------------------------------'''

data = pd.read_csv('data.csv')
print(data.to_string())
# to_string() : print the entire DataFrame.

#If you have a large DataFrame with many rows,
#  Pandas will only return the first 5 rows,
#  and the last 5 rows

''' max_rows '''
print(pd.options.display.max_rows)
# 60
# In this system the number is 60, which means that if the DataFrame
#  contains more than 60 rows, the print(df) statement will return
#  only the headers and the first and last 5 rows.

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')

print(df) 