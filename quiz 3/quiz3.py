
import os
#os.chdir(r'Teams\General\Files\Class Materials')
os.chdir(r'D:\GU\Programming Principles')
def readfile():
    filename = input("Enter a filename: ")
    
    try:
        file1 =  open(filename, 'r')
    except Error:
        exit(1)
    file2 = open('test_file_result.txt', 'w')
    for line in file1: 
        if ':' in line: continue
        file2.writelines(line)
        
    file1.close()
    file2.close()
  
readfile()