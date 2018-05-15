# Functions

######## 1. Defining Functions #######

def cylinder_volume(height, radius=5):
	pi = 3.1415926
	return height*pi*radius**

cylinder_volume(10) 
cylinder_volume(10,7) # override the default argument
cylinder_volume(height=10, radius=7) # another way to write


# write a function to return a string says how many weeks and days that is
def readable_timedelta(days):
	weeks = days / 7
	remainder = days % 7
	return '{} week(s) and {} day(s).'.format(weeks, remainder)

######## 2. Documentation #######

def readable_timedelta(days):
    """
    Print the number of weeks and days in a number of days.

    Parameters:
    days -- number of days to convert (int)

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)


######## 3. Variable Scope #######
"""
variable scope refers to which parts of a program a variable can be used
it's best to define variables in the smallest scope they will be needed in
"""
egg_count = 0
def buy_eggs():
	egg_count + = 12
buy_eggs()

# Output: not 12 but error (UnboundlocalError) since python doesn't allow functions to modify variables that are outside the function's scope
# A revised way:
egg_count = 0
def buy_eggs(count): # buy a dozen eggs
	return count + 12

egg_count = buy_eggs(egg_count)


######## 4. Lambda Expressions #######
# use lambda expressions to create anonymous functions

double = lambda x: x * 2 
multipy = lambda x , y : x * y
multipy(4,7)

# lambda with Filter()

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)

# Output: ['Chicago', 'Denver', 'Boston']

######## 5. Iterators and Generators #######
"""
Iterables are objects that can return one of their elements at a time, such as a list. 
Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.
An iterator is an object that represents a stream of data. 
This is different from a list, which is also an iterable, but not an iterator because it is not a stream of data.

Why Generators?

Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory,
or when the cost to calculate each list element is high and you want to do it as late as possible. 
But they can only be iterated over once.
"""

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# Output:
"""
Lesson 1: Why Python Programming
Lesson 2: Data Types and Operators
Lesson 3: Control Flow
Lesson 4: Functions
Lesson 5: Scripting
"""


