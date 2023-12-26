file = open('Test1.txt','r') #reading the file content single line or multiple lines 
# content = file.read()  
# line = file.readline()  
lines = file.readlines()
print(lines)
file.close()

