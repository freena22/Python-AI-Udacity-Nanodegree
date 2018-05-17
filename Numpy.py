# Numpy

""" Why Use Numpy?

Numpy can make a difference of orders of magnitude in computation time.

Use numpy array to holds the pixel values of an image that will be fed into a model for image classification

NumPy is that it has multidimensional array data structures that can represent vectors and matrices. 
A lot of machine learning algorithms rely on matrix operations. 
For example, when training a Neural Network, you often have to carry out many matrix multiplications. 
NumPy is optimized for matrix operations and it allows us to do Linear Algebra operations effectively and efficiently, 
making it very suitable for solving machine learning problems.

"""
import time
import numpy as np

x = np.random.random(100000000)

start = time.time()
sum(x) / len(x)
print(time.time() - start)

# Output: 7.319624900817871

start = time.time()
np.mean(x)
print(time.time() - start)

# Output: 0.04637503623962402


############### Creating Numpy ndarrays ################


x = np.array([1,2,3,4,5])  # 1D ndarray that contains only integers
print('x = ', x)  # x = [1,2,3,4,5]

x.shape   # (5,)

type(x)   # 'numpy.ndarray'

x.dtype   # int64  -- tells us that the elements of x are stored in memory as signed 64-bit integers

x = np.array([1,2,'World'])

x.shape   # (3,)

x.dtype   # U21  -- even though with mixed data types, the elements in x are all of the same type: unicode strings of 21 characters

##### Saving ndarray

# save x into the current directory as
np.save('my_array', x)

# load the saved array from current directory into variable y

y = np.load('my_array.npy')

########## Using Built-in Functions to Create ndarrays ##########

# create matrixs
x = np.zero((3,4))

x = np.ones((3,2))

x = np.full((2,3), 5 dtype = float)

x = np.eye(5). # creates a square N x N ndarray corresponding to the identity matrix 
               # identity matrix: a square matrix that has only 1s in its main diagonal and zeros everywhere else.

x = np.diag([10,20,30,50]). # creates an ndarray corresponding to the diagonal matrix 

# np.arange()

x = np.arange(1,20,2). # Out: [ 1  3  5  7  9 11 13 15 17 19]

# np.linspace()

x = np.linspace(0,25,10)

# Out: [ 0.          2.77777778  5.55555556  8.33333333 11.11111111 13.88888889
# 16.66666667 19.44444444 22.22222222 25.        ]

# np.reshape()  converts any Numpy array into a specified shape

x = np.arange(20)  # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
x = np.reshape(x, (4,5))
"""
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
"""

x = np.arange(20).reshape((4,5)). # in one line code

x = np.random.randint(4,15,size=(3,2))

x = np.random.normal(0, 0.1, size=(1000,1000)) # for normal distribution

########## Accessing, Deleting, and Inserting Elements Into ndarrays ##########

x = np.array([1,2,3,4,5])

print('1st element: ', x[0])

# change the element
x[3] = 20

# change in matrix
x = np.arange(1,10).reshape(3,3)

print('Element at (0,1):', x[0,1])

# delete the element

np.delete(Y, 0, axis = 0)  # delete the first row of y
np.delete(Y, [0,2], axis = 1)  # delete the first and last column of y


# append the integer 7 and 8 to x
np.append(x, [7,8])

# insert the integer 3 and 4 between 2 and 5 in x
np.insert(x,2,[3,4])

# stack ndarrays on top of each other -- vertical stacking
np.vstack((x,Y))  # stack x on top of Y

# stack ndarrays side by side  --  horizontal stacking

np.hstack((Y, x.reshape(2,1)))  # stack x on the right of Y, we need to reshape x in order to stack it on the right of Y

################ Slicing ndarrays ###################

Z = X[1:4, 2:5]

# X and Z are now just two different names for the same ndarray.
# If we make changes in Z it will be in effect changing the elements in X as well.

# If we want to create a new ndarray that contains a copy of the values we need to use np.copy()

Z = np.copy(X[1:4, 2:5])

# extract only the unique elements in an ndarray 
np.unique(X)


############## Boolean Indexing, Set Operations, and Sorting ##############

# use Boolean indexing to assign the elements that are between 10 and 17 the value of -1
X[(X > 10) & (X <17)] = - 1

np.intersect1d(x,y) # elements both in x and y

np.setdiff1d(x,y) # elements in x but not in y

np.union1d(x,y) # all the elemnts of x and y

# sort x but only keep the unqiue elements in x

np.sort(np.unique(x))

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive)
# Use Boolean indexing to pick out only the odd numbers in the array

X = np.arange(1,26).reshape(5,5)
Y = X[X % 2 != 0]

############## Arithmetic operations and Broadcasting ##############

# use Broadcasting to create a 4 x 4 ndarray that has its first column full of 1s, second column full of 2s...
X = np.ones((4,4)) * np.arange(1,5)







