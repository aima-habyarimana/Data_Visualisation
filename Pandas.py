'''
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
'''

'''
import pandas as pd

print(pd.__version__)
'''

'''
# A Pandas Series is like a column in a table.
# If nothing else is specified, the values are labeled with their index number. 
# First value has index 0, second value has index 1 etc.
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])
'''


'''
# Create your own labels. 

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print(myvar["y"])
'''

'''
# Key/Value Objects as Series
# Note: The keys of the dictionary become the labels.
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
'''

'''
# Create a Series using only data from "day1" and "day2"
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
'''

'''
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

# Pandas use the loc attribute to return one or more specified row(s)
print(myvar.loc[0]) # Note: This example returns a Pandas Series.

#use a list of indexes:
print(myvar.loc[[0, 1]]) #Note: When using [], the result is a Pandas DataFrame.
'''

'''
# With the index argument, you can name your own indexes.
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

#refer to the named index:
print(df.loc["day2"])
'''


'''
import pandas as pd

df = pd.read_csv('C:/Users/User/Desktop/AWS Generation/Python/pythonProject/data.csv')

print(df.to_string())
'''

'''
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')

print(df.to_string())   # Tip: use to_string() to print the entire DataFrame. 
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
'''

'''
# Print the DataFrame without the to_string() method.
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')

print(df)

'''


'''
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''

'''
# Get the path of a particular file or directory
import os
print('File name :    ', os.path.basename('data.csv'))
print('Directory Name:     ', os.path.dirname('AWS Generation'))
'''

'''
# number of maximum rows returned.
# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
# You can change the maximum rows number with the same statement.

import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999
print(df)
'''


'''

# Read JSON file
import pandas as pd

df = pd.read_json('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.json')
print(df)   Tip: use to_string() to print the entire DataFrame.
'''

'''
# If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
import pandas as pd

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
'''

'''
# Analyzing Dataframes
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
print(df.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head())

print(df.tail())

print(df.info())

# 5 rows with no value at all, in the "Calories" column, for whatever reason. Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data

'''


'''
# Data cleaning means fixing bad data in your data set.
# Bad data could be:
# Empty cells
# Data in wrong format
# Wrong data
# Duplicates


# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
new_df = df.dropna()

print(new_df.to_string())
'''


'''

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:

import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
df.dropna(inplace = True)
print(df.to_string())

# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

'''

'''
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

# Replace NULL values with the number 130:
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
df.fillna(130, inplace = True)

# df["Calories"].fillna(130, inplace = True)  # Replace NULL values in the "Calories" columns with the number 130:
print(df.to_string())

'''

'''
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
# Calculate the MEAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
print(df.to_string())
# Mean = the average value (the sum of all values divided by number of values).

'''

'''
# Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)
print(df.to_string())
# Median = the value in the middle, after you have sorted all values ascending.

'''

'''
# Calculate the MODE, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)
print(df.to_string())
# Mode = the value that appears most frequently.
'''

'''
# Discovering Duplicates with duplicated()
import pandas as pd
df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
print(df.duplicated())
# To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace = True)
'''

''' 
# Pandas - Data Correlations - The corr() method calculates the relationship between each column in your data set.
# df.corr()
# Note: The corr() method ignores "not numeric" columns.

import pandas as pd
df = pd.read_csv('C:\\Users\\User\\Desktop\\AWS Generation\\Python\\pythonProject\\data.csv')
print(df.corr())

# Result Explained
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
# The number varies from -1 to 1.
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
# 0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.
# -0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.
# 0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.
# What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

Perfect Correlation:
We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself.

Good Correlation:
"Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

Bad Correlation:
"Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.

'''





