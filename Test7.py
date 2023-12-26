import os
import os.path
import shutil

#folder deletion recusrively 

list = os.listdir('.')
print(*list,sep='\n')

shutil.rmtree('Test_folder3')
print('Test_folder3 has been removed successfully. PFB existing list')

list = os.listdir('.')
print(*list,sep='\n')



