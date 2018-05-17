# Pandas

"""
Pandas series is a one-dimensional array-like object that can hold many data types.
One of the main differences between Pandas Series and NumPy ndarrays is that you can assign an index label to each element in the Pandas Series. 
Another big difference between Pandas Series and NumPy ndarrays is that Pandas Series can hold data of different data types.
"""

import pandas as pd

groceries = pd.Series(data = [30, 6, 'Yes', 'No'], index = ['eggs', 'apples', 'milk', 'bread'])

groceries

""" Output:
eggs           30
apples         6
milk         Yes
bread       No
dtype: object
"""

groceries.shape # (4,)

groceries.ndim  # 1

groceries.size  # 4 elements

groceries.values

groceries.index 

'bananas' in groceries  # False

########## Accessing ##########

groceries['eggs']  # accessing elements with index labels

groceries[['milk', 'bread']]  # insert a list for multiple index

# .loc  -- stand for location ans it's used to explicitly state that using a labled index

groceries.loc[['eggs','apples']]


# iloc

# use iloc to access multiple numerical indices
groceries.iloc[[2,3]]  # out: milk -- yes  bread -- no


groceries['eggs'] = 2  # change the number of eggs to 2

groceries.drop('apples', inplace = True)

########## Arithmetic Operations on Pandas Sereis ##########

fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])




