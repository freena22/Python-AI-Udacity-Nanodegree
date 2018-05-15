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
# variable scope refers to which parts of a program a variable can be used
# it's best to define variables in the smallest scope they will be needed in

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



######## 5. Iterators and Generators #######