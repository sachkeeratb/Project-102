import time
import os
import shutil

print("Enter your Microsoft username.")

x = input()

path = "/Users/",x,"/Documents/NewFolder"
days = time.time()
num_of_days = 3 * (3600*24)

if os.path.exists(path):

    list_of_files = os.listdir(path)
    for file in list_of_files:
        ext = os.path.splitext(file)

        ext = ext[1:]
        if ext=='' :
            continue
        file_location = os.path.join(path+'/',file)
        date = os.stat(file_location).st_mtime
        
        print(days-date,'    ',date,'    ',days,'    ',num_of_days)
        
        if days-date > num_of_days:
                if not ext == '':
                    print(file_location)
                    os.remove(file_location)
else:
    print("Not Found")
