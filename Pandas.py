# Pandas

""" Creating Pandas Series
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

fruits + 2 

fruits / 2

import numpy as np
np.sqrt(fruits)
np.exp(fruits)
np.power(fruits, 2)  # 100 36 9

fruits['bananas'] + 2 # 5
fruits.iloc[0] - 2 # 8
fruits.loc[['bananas', 'oranges']] / 2  # 5.0 3.0

########## Creating Pandas DataFrames ##########

items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

print(type(items))  # dict

shopping_cart = pd.DataFrame(items)
shopping_cart

"""
	    Alice	Bob
bike	500.0	245.0
book	40.0	NaN
glasses	110.0	NaN
pants	45.0	25.0
watch	NaN	    55.0

"""

shopping_cart.values

shopping_cart.ndim # 2

shopping_cart.size  # 10

bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

"""
	    Bob
bike	245
pants	25
watch   55

"""

sel_shopping_cart = pd.DataFrame(items, index=['pants', 'book'])

"""
	Alice	Bob
pants	45	25.0
book	40	NaN

"""

alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

# We display the DataFrame
store_items

"""
     bikes	glasses	 pants	watches
store 1	    20	      NaN	30	35
store 2	    15	      50.0	5	10
"""

########## Accessing Elements ##########

store_items[['bikes','glasses']]  # access the colomns

store_items.loc[['store 1']]  # acess the row

store_items['bike']['store 1']  # colums label should comes first  # Out： 1

##### add new colomn

store_items['shirt'] = [15,2]

store_items['suits'] = store_items['pants'] + store_items['shirts']

##### add new row 

# We create a dictionary from a list of Python dictionaries that will number of items at the new store
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3'])

store_items = store_items.append(new_store)

# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

# we display the modified DataFrame
store_items

"""
bikes	glasses	pants	shirts	shoes	suits	watches	new watches
store 1	 20	    NaN	    30	    15.0	8	    45.0	35	NaN
store 2	 15	    50.0	5	    2.0	    5	    7.0	    10	10.0
store 3	 20	    4.0	    30	    NaN	    0	    NaN	    35	35.0
"""

store_items.pop('new watches')

store_items = store_items.drop(['watches', 'shoes'], axis = 1)


# We change the column label bikes to hats
store_items = store_items.rename(columns = {'bikes': 'hats'})

# We change the row label from store 3 to last store
store_items = store_items.rename(index = {'store 3': 'last store'})


# We change the row index to be the data in the pants column
store_items = store_items.set_index('pants')


########## Dealing with NaN ##########

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items

"""
bikes	glasses	pants	shirts	shoes	suits	watches
store 1	20	    NaN	     30	     15.0	8	45.0	35
store 2	15	    50.0	 5	     2.0	5	7.0	    10
store 3	20	    4.0	    30	     NaN	10	NaN	    35
"""

x = store_items.isnull()
print(x)

"""
bikes	glasses	pants	shirts	shoes	suits	watches
store 1	False	True	False	False	False	False	False
store 2	False	False	False	False	False	False	False
store 3	False	False	False	True	False	True	False
"""

x = store_items.isnull().sum().sum() # 3

store_items.count()

store_items.dropna(axis=0)

#         bikes  glasses  pants  shirts  shoes  suits  watches
# store 2     15     50.0      5     2.0      5    7.0       10

store_items.dropna(axis=1)

store_items.fillna(0)

store_items.fillna(method='ffill', axis = 0)
# use the forward filling (ffill) method to replace NaN values using the previous known value along the given axis.

# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)

# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)

# We replace NaN values by using linear interpolation using column values
# use linear interpolation to replace NaN values using the values along the given axis. 
store_items.interpolate(method = 'linear', axis = 1)

"""
         bikes  glasses  pants  shirts  shoes  suits  watches
store 1   20.0     25.0   30.0    15.0    8.0   45.0     35.0
store 2   15.0     50.0    5.0     2.0    5.0    7.0     10.0
store 3   20.0      4.0   30.0    20.0   10.0   22.5     35.0

"""

########### Practice ##############

import pandas as pd
import numpy as np

# Since we will be working with ratings, we will set the precision of our 
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Create a dictionary with the data given above
dat = {'Book Title' : books,
       'Author' : authors,
       'User 1' : user_1,
       'User 2' : user_2,
       'User 3' : user_3,
       'User 4' : user_4}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)
book_ratings

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:
book_ratings.isnull().sum()
book_ratings.fillna(book_ratings.mean(), inplace=True)









