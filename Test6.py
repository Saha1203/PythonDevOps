import os
import os.path


list = os.listdir('.')
print(*list,sep='\n')

os.remove('Test2.txt')

list = os.listdir('.')
print(*list,sep='\n')
