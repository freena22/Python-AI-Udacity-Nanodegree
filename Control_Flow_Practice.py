##### Control Flow #####

# 1. Boolean Expressions for Conditions

points = 174

# set prize to default value of None

prize = None

if points <= 50:
	prize = 'wood rabbit'
elif 151 <= points <= 180:
	prize = 'wafer-thin mint'
elif points >= 181:
	prize = 'penguin'

# use the truth value of prize to assign result to the correct message
if prize:  # NOT!! If prize = TRUE
	result = 'Congratulations! You won a {}!'.format(prize)
else:
	result = 'Oh dear, no prize this time'

print(result)

# 2. For Loop

########## Practice 1 ############

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.lower().replace(" ", "_")
    usernames.append(name)

########## Practice 2 ############

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

########## Practice 3 ############

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result


for fruit, count in basket_items.items():
   if fruit in fruits:
       result += count

print("There are {} fruits in the basket.".format(result))

# 3. While Loops

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)


