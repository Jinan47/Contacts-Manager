import os


# path for all the code
dir_path = 'C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts'


# create a new path
new_path = 'C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts\\new_path'


# create the file that will be in the new path
file_new_path = 'new for new'


# join the new file with the new path
new_join = os.path.join(new_path, file_new_path)


# make the new_join real
os.makedirs(new_join)


# print a successful
print("Directory '% s' created" % file_new_path)



# create the file path that join the path with the file
path_file = os.path.join('C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts', 'I worked !.txt')


# print a successful
print("Directory '% s' created" % 'I worked !.txt') 


# deal with the possiblety of the 'non exist path' error
if not os.path.exists('C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts'):
    os.makedirs('C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts')

f = open(path_file, "a")

# # file existing (True/False)
# file_exist = os.path.exists('C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts\\c.txt')
# print(file_exist)


# create a file in a specific path 
def safe_open_w(path):
    # Open "path" for writing, creating any parent directories as needed.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')


with safe_open_w('C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts\\c.txt') as f:
    f.write('C:\\Users\\Jinan\\OneDrive\\Desktop\\Projects\\My own projects\\Contacts Project\\Contacts\\c.txt')
    print("Directory 'c.txt' created")
    
    
     
# list the files and folders found 
dir_list = os.listdir(dir_path)
  
print('Files and directories in "Contacts" ', dir_path, ":")
       
print(dir_list)


