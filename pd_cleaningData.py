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
print(new_df)

# dropna() method returns a new DataFrame, 
# and will not change the original

# to change the original DataFrame, 
# use the inplace = True argument

df.dropna(inplace = True)
print(df)


''' Replace Empty Values'''
#fillna()
df = pd.read_csv('dataA.csv')
df.fillna(130, inplace=True)
print(df.to_string())


''' Replace Only For Specified Columns '''

df = pd.read_csv('dataA.csv')
df["Calories"].fillna(130, inplace = True)
print(df.to_string())


''' Replace Using Mean, Median, or Mode '''
# Calculate the MEAN, and replace any empty values with it
df = pd.read_csv('dataA.csv')
x = df["Calories"].mean() # or median()
df["Calories"].fillna(x, inplace = True)
print(df.to_string())

# Mean = the average value (the sum of all values divided
#  by number of values)

# Median = the value in the middle,
#  after you have sorted all values ascending.

#mode()[]
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())
# Mode = the value that appears most frequently.

'''--------------------------------------------------------------'''
'''-------------      Cleaning Wrong Format      ----------------'''
'''--------------------------------------------------------------'''



'''--------------------------------------------------------------'''
'''-------------       Cleaning Wrong Data       ----------------'''
'''--------------------------------------------------------------'''



'''--------------------------------------------------------------'''
'''---------------      Removing Duplicates      ----------------'''
'''--------------------------------------------------------------'''
