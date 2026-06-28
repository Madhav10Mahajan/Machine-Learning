# file handling 
# performing file operations

import os

file_path = os.path.join(os.path.dirname(__file__), 'example.txt')

# reading files
with open(file_path,'r') as file:
    content=file.read()
    print(content)

# writing files overrides the existing text
with open(file_path,'w') as file:
    file.write('hello world\n')
    file.write('this is a new line\n')

# appending text in files
with open(file_path,'a') as file:
    file.write('this line gets appended at the end\n')

# writing a list of lines
lines=['First line\n', 'second line\n', 'third line\n']

with open(file_path,'a') as file:
    # for line in lines:
    #     file.write(line)
    file.writelines(lines)

# writing and then reading
# w+ mode is used for both reading and writing, if the file doesnt not exist it creates the file and then writes else it overwrides then existing content

with open(file_path,'w+') as file:
    file.write('Hello World\n')
    file.write('this is the second line\n')
    
    ## move the file cursor
    # move the cursor to the beginning
    file.seek(0) # moves the cursor to the beginning
    content=file.read()
    print(content)