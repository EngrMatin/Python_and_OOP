import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'

postfix = [1, 2, 3]

while True:
    source_object = glob.glob(source_path)             # <class 'list'>
    # print(source_object)

    if len(source_object) > 0:

        object_path = source_object[0]
        shutil.copy(object_path, '.')

        object_name = object_path.split('\\')[-1].split('.')                 # <class 'list'>
        prefix = object_name[0]
        postfix2 = object_name[1]
        # print(object_name)
        

        for item in range(len(postfix)):
            filename = prefix + '_' + str(item) + '.' + postfix2
            # print(filename)
            shutil.copy(object_path, f"{destination_path}/{filename}")

        os.remove(object_path)
        os.remove(object_path.split('\\')[-1])