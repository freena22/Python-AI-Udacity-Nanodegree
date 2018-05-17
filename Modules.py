# Modules

"""
To avoid running executable statements in a script when it's imported as a module in another script, 
include these lines in an if __name__ == "__main__" block. 
Or alternatively, include them in a function called main() and call this in the if main block.
"""

# demo.py

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)   # Output: __main__
print(uf.__name__)  # Output: useful_functions



# useful_functions.py

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()


"""
Write a function called generate_password that selects three random words from the list of words word_list
and concatenates them into a single string. 
"""

import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    return ''.join(random.sample(word_list,3))


# test your function
print(generate_password())



# Techniques for Importing Modules

import module_name

from module_name import object_name as new_name

from module_name import first_object, second_object


