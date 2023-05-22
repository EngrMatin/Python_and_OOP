import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'

postfix = [1, 2, 3]

source_obj_list = glob.glob(source_path)
# print(source_obj_list)
# print(type(source_object))         # <class 'list'>

obj1 = source_obj_list[0]
server_obj1 = shutil.copy(obj1, '.')
content_list = open(server_obj1, 'r').readlines()

obj1_name_list = obj1.split('\\')[-1].split('.')
# print(obj1_name_list)
prefix = obj1_name_list[0]
postfix2 = obj1_name_list[1] 

for item in range(len(postfix)):
    filename = prefix + '_' + str(item+1) + '.' + postfix2
    # print(filename)          # <class 'str'>
    
    dest_obj = shutil.copy(server_obj1, f"{destination_path}/{filename}")
    open(dest_obj, 'w').writelines(content_list[0 : (item+1)*10])


# os.remove(obj1)
# os.remove(obj1.split('\\')[-1])