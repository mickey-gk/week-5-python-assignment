# creating a file :
try:
    with open('my_file.txt', 'w') as file:
        file_name = file.name  # get the file name
        data = f'--------------------------------------------\n\
date: 23rd-sep-2024 \tFILE NAME: {file_name} \n\
--------------------------------------------\n'
        file.write(data)
except PermissionError:
    print('error: permission required to write to this file')
else:
    print(f'file: {file_name} -- created successful --\n')

# open file for reading
try:
    with open(file_name, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f'error: could not find the file: {file_name}')
else:
    print("READING DATA FROM MY FILE...")
    print(content)

# append data to my_file
try:
    with open(file_name, 'a') as file:
        data = 'person\'s data: \n'
        file.write(data)
        data ="details: {'name': 'mickey', 'gender': 'male'} \n"
        file.write(data)
except FileNotFoundError:
    print(f'error: failed to open the file {file_name}')
else:
    print(f'data appended to file: {file_name}')
finally:
    print('quiting program!')