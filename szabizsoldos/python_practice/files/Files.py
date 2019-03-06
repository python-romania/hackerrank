
# coding: utf-8

# In[24]:


import os, shutil

path_folder_X= 'C:/Users/szabi.zsoldos/PycharmProjects/MMM/hackerrank/szabizsoldos/python_practice/'
path_folder_Y= 'C:/Users/szabi.zsoldos/PycharmProjects/MMM/hackerrank/szabizsoldos/python_practice/'
if not os.listdir(path_folder_X) or not os.listdir(path_folder_Y):
    print("One of the folder is empty")
else:
    if os.listdir(path_folder_X)==os.listdir(path_folder_Y):
       
        for the_file in os.listdir(path_folder_X):
                file_path = os.path.join(path_folder_X, the_file)
                print(file_path)
        print("Ready")
    else: 
        print("The folders are not equal")
      
        

