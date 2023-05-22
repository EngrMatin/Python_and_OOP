import glob
import shutil
import os
from zipfile import ZipFile

source_path = '../source/*'
destination_path = '../destination'

postfix = [1, 2, 3]

source_obj_list = glob.glob(source_path)

obj1 = source_obj_list[0]
server_obj1 = shutil.copy(obj1, '.')
content_list = open(server_obj1, 'r').readlines()

obj1_name_list = obj1.split('\\')[-1].split('.')
prefix = obj1_name_list[0]
postfix2 = obj1_name_list[1] 

for i in range(len(postfix)):
    filename = prefix + '_' + str(i+1) + '.' + postfix2
    
    dest_obj = shutil.copy(server_obj1, f"./converted_files/{filename}")
    open(dest_obj, 'w').writelines(content_list[0 : (i+1)*10])


file_paths = []
directory = './converted_files'
for root, directories, files in os.walk(directory):
    for filename in files:
        filepath = os.path.join(root, filename)
        file_paths.append(filepath)

with ZipFile('converted_files.zip','w') as zip:
    for file in file_paths:
        zip.write(file)

file_name2 = "converted_files.zip"
shutil.move(file_name2, f"{destination_path}/{file_name2}")

file_name3 = "../destination/converted_files.zip"
with ZipFile(file_name3, 'r') as zip:
    zip.extractall(destination_path)
    

# os.remove(obj1)
# os.remove(obj1.split('\\')[-1])
# os.remove(file_name3)