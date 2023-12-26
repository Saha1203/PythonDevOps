import os
import os.path
#folder deletion commands 
# os.mkdir('Test_folder2')
list = os.listdir('.')
print(*list,sep='\n')


filePath = os.path.exists('Test_folder3')
print('The existance of the Test_folder3 is : ',filePath)

os.rmdir('Test_folder2')
list = os.listdir('.')
print(*list,sep='\n')

