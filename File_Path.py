import os.path

if os.path.isfile('File.txt'):
    print ('存在')
    file = open('File.txt','a')
    file.write("Yay. I have a new file!")
    file.close()
else:
    print ('不存在')
    file = open("File.txt",'w')
    file.write("This is a new file.")
    
    file.close()