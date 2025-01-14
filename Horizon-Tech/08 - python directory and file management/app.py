import os

# looking current directory
print(os.getcwd()) #C:\Learn\Learn-Python\Horizon-Tech\08 - python directory and file management
print(os.getcwdb()) #b'C:\\Learn\\Learn-Python\\Horjson-Tech\\08 - python directory and file management'


# Create the new directory
os.mkdir('new_dir_01')

# Rename the directory
# os.rename('new_dir_0', 'new_dir_02') # FileNotFoundError: [WinError 2] The system cannot find the file specified: 'new_dir_0' -> 'new_dir_02'
os.rename('new_dir_01', 'my_new_dir_02')

# List the file and directory in the current directory
print(os.listdir()) # ['app.py', 'my_new_dir_02']

# Remove the directory and file
# os.rmdir('my_new_dir_00') # FileNotFoundError: [WinError 2] The system cannot find the file specified: 'my_new_dir_00'
os.rmdir('my_new_dir_02')
os.rmdir('new_dir_01')

# change the directory
print(os.getcwd())
os.chdir('C:\\Learn\\Learn-Python\\Horizon-Tech')
print(os.listdir())