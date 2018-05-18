# Reading files

f = open('my_path/my_file.txt','r')  # default is 'r'
file_data = f.read()
f.close()  # use the close method to free up any system resources taken up by the file

# Writing to a file

f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

# With method - allows you to open a file, do operations on it, and automatically close it after the indented code is executed

with open('my_path/my_file.txt', 'r') as f:
	file_data = f.read()

""" camelot.txt
We're the knights of the round table
We dance whenever we're able
"""

with open(camelot.txt) as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

""" Output
We
're the 
knights of the round table
We dance whenever we're able
"""

f.readline() # read \n as newline 

# .strip() 

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

# Output: ["We're the knights of the round table", "We dance whenever we're able"]


def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

