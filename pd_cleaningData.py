import pandas as pd

# Data Cleaning
# Data cleaning means fixing bad data in your data set.

    # Bad data could be:
        # Empty cells
        # Data in wrong format
        # Wrong data
        # Duplicates

'''--------------------------------------------------------------'''
'''-------------      Cleaning Empty Cells       ----------------'''
'''--------------------------------------------------------------'''

# remove rows that contain empty cells
# Return a new Data Frame with no empty cells

df = pd.read_csv('data.csv')
new_df = df.dropna()
#print(new_df)

# dropna() method returns a new DataFrame, 
# and will not change the original

# to change the original DataFrame, 
# use the inplace = True argument

df.dropna(inplace = True)
#print(df)


''' Replace Empty Values'''
#fillna()
df = pd.read_csv('dataA.csv')
df.fillna(130, inplace=True)
#print(df.to_string())


''' Replace Only For Specified Columns '''

df = pd.read_csv('dataA.csv')
df["Calories"].fillna(130, inplace = True)
#print(df.to_string())


''' Replace Using Mean, Median, or Mode '''
# Calculate the MEAN, and replace any empty values with it
df = pd.read_csv('dataA.csv')
x = df["Calories"].mean() # or median()
df["Calories"].fillna(x, inplace = True)
#print(df.to_string())

# Mean = the average value (the sum of all values divided
#  by number of values)

# Median = the value in the middle,
#  after you have sorted all values ascending.

#mode()[]
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
#print(df.to_string())
# Mode = the value that appears most frequently.

'''--------------------------------------------------------------'''
'''-------------      Cleaning Wrong Format      ----------------'''
'''--------------------------------------------------------------'''

df = pd.read_csv('dataA.csv')
# df.dropna(subset=['Date'], inplace = True)
        # Remove rows with a NULL value in the "Date" column
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

#print(df.to_string())

'''--------------------------------------------------------------'''
'''-------------       Cleaning Wrong Data       ----------------'''
'''--------------------------------------------------------------'''


'''Replacing values'''

df = pd.read_csv('data.csv')
# df.loc[7,'Duration'] = 45

# print(df.to_string())

# For small data sets we might be able to replace the wrong data
#  one by one, but not for big data sets.

# To replace wrong data for larger data sets you can create some
#  rules, e.g. set some boundaries for legal values, and replace
#  any values that are outside of the boundaries.


df = pd.read_csv('dataA.csv')
for x in df.index:
    if df.loc[x, "Duration"]>120:
        df.loc[x,"Duration"] = 120
print(df.to_string())


''' Removing Rows '''

df = pd.read_csv('dataA.csv')
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)

print(df.to_string())

'''--------------------------------------------------------------'''
'''---------------      Removing Duplicates      ----------------'''
'''--------------------------------------------------------------'''
df = pd.read_csv('dataA.csv')
print(df.duplicated())

# 0     False
# 1     False
# 2     False
# 3     False
# 4     False
# 5     False
# 6     False
# 7     False
# 8     False
# 9     False
# 10    False
# 11    False
# 12     True
# 13    False
# 14    False
# 15    False
# 16    False
# 17    False
# 18    False
# 19    False
# 20    False
# 21    False
# 22    False
# 23    False
# 24    False
# 25    False
# 26    False
# 27    False
# 28    False
# 29    False
# 30    False
# 31    False
# dtype: bool


''' drop duplicate '''

df = pd.read_csv('data.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())
