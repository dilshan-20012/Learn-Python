import os

# looking current directory
print(os.getcwd()) #C:\Learn\Learn-Python\Horizon-Tech\08 - python directory and file management
print(os.getcwdb()) #b'C:\\Learn\\Learn-Python\\Horjson-Tech\\08 - python directory and file management'


# Create the new directory
os.mkdir('new_dir_01')

# Rename the directory
# os.rename('new_dir_0', 'new_dir_02') # FileNotFoundError: [WinError 2] The system cannot find the file specified: 'new_dir_0' -> 'new_dir_02'
os.rename('new_dir_01', 'my_new_dir_02')