# import numpy
# arr = numpy.array([1, 2, 3, 4, 5])
# print(arr)

'''
# 0-D (Dimension) Arrays. 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
import numpy as np
arr = np.array(42)
print(arr)
'''

'''
# 1-D Arrays
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
'''


'''
# 2-D Arrays. NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
'''

'''
# 3-D arrays. Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

'''
'''
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
'''


'''
# When the array is created, you can define the number of dimensions by using the ndmin argument.
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
'''
'''
# You can access an array element by referring to its index number.
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

'''

'''
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
'''

'''
# Access the third element of the second array of the first array:
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
'''

'''
# Use negative indexing to access an array from the end.
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])
'''


'''
# Slice from the index 3 from the end to index 1 from the end:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
'''

'''
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

'''

'''
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)
'''


'''
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
'''

'''
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
'''


'''
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
'''

'''
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this. 
# Convert the array into a 1D array:

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
'''

'''
# iterate elements

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


'''


'''
# Iterating Arrays Using nditer()
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)
'''

'''
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

'''

'''
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
'''


'''
# We pass a sequence of arrays that we want to join to the concatenate() function
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
'''


'''
# Join two 2-D arrays along rows (axis=1):
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
'''

'''
# NumPy provides a helper function: hstack() to stack along rows.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
'''


'''
# NumPy provides a helper function: vstack()  to stack along columns.
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
'''


'''
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
'''


'''
# You can search an array for a certain value, and return the indexes that get a match.

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)

# Find the indexes where the values are even:
# x = np.where(arr%2 == 0)

print(x)
'''


'''
# Sort an array
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
'''


'''
# If you use the sort() method on a 2-D array, both arrays will be sorted:
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
'''



'''
# Getting some elements out of an existing array and creating a new array out of them is called filtering. 
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.
# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

'''

'''
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.
# Create a filter array that will return only values higher than 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
'''


'''
# Create a filter array that will return only values higher than 42:
import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
'''


'''
# Generate a random integer from 0 to 100:
from numpy import random
x = random.randint(100)
print(x)


# Generate a random float from 0 to 1:
from numpy import random
x = random.rand()
print(x)


# Generate a 1-D array containing 5 random integers from 0 to 100:
from numpy import random
x=random.randint(100, size=(5))
print(x)


# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)


# The choice() method allows you to generate a random value based on an array of values.
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)
'''

'''
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0

from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)


The sum of all probability numbers should be 1.

Even if you run the example above 100 times, the value 9 will never occur.

You can return arrays of any shape and size by specifying the shape in the size parameter.

Same example as above, but return a 2-D array with 3 rows, each containing 5 values.

from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

'''


'''
# The NumPy Random module provides two methods for this: shuffle() and permutation()
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)



arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
'''


'''
# Add the values in arr1 to the values in arr2:
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)


import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)
# newarr = np.subtract(arr1, arr2)
# newarr = np.multiply(arr1, arr2)
# newarr = np.divide(arr1, arr2)
# newarr = np.power(arr1, arr2)
# newarr = np.mod(arr1, arr2) or newarr = np.remainder(arr1, arr2)
# newarr = np.divmod(arr1, arr2)
# newarr = np.absolute(arr) 

print(newarr)

'''
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
import numpy as np

arr = np.trunc([-3.1666, 3.6667])

print(arr)

arr = np.fix([-3.1666, 3.6667])

print(arr)


# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
import numpy as np

arr = np.around(3.1666, 2)

print(arr)


# The floor() function rounds off decimal to nearest lower integer.
import numpy as np

arr = np.floor([-3.1666, 3.6667])

print(arr)


# The ceil() function rounds off decimal to nearest upper integer.
import numpy as np

arr = np.ceil([-3.1666, 3.6667])

print(arr)


# Sum the values in arr1 and the values in arr2:
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)


# To find the product of the elements in an array, use the prod() function.
import numpy as np
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)


# Compute discrete difference of the following array:
import numpy as np
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)

# Convert following array with repeated elements to a set:
import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)


# Find union of the following two set arrays:
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)


# Find intersection of the following two set arrays:
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)