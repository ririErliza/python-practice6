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
#print(data.to_string())
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

#print(df)

'''--------------------------------------------------------------'''
'''-------------------      Read JSON       ---------------------'''
'''--------------------------------------------------------------'''

# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object,
#  and is well known in the world of programming, including Pandas.

jdata = pd.read_json('jdata.json')
#print(jdata.to_string())



''' Dictionary as JSON '''
# JSON objects have the same format as Python dictionaries.
# If your JSON code is not in a file, but in a Python Dictionary,
#  we can load it into a DataFrame directly

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df)


'''--------------------------------------------------------------'''
'''-------------      Analyzing DataFrames       ----------------'''
'''--------------------------------------------------------------'''

#viewing the data

# head() method
    # returns the headers and a specified number of rows,
    #  starting from the top.

vdat = pd.read_csv('data.csv')
print(vdat.head(10)) # from index 0 to 9

# tail() method
    # returns the headers and a specified number of rows,
    #  starting from the bottom.

print(vdat.tail())


''' Info About the Data '''
print(vdat.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 154 entries, 0 to 153
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  154 non-null    int64
#  1   Pulse     154 non-null    int64
#  2   Maxpulse  154 non-null    int64
#  3   Calories  149 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 4.9 KB
# None

