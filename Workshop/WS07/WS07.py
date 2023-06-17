import os

os.chdir(r'D:\GU\Programming Principles\Workshop\WS07')

emptyline =0
f1 = open("P1_v2.txt", "r").readlines()
f2 = open("string_doc_nonempty.txt", "w")
for i in f1:
    if not i.isspace(): f2.write(i)
    else: emptyline+=1
f2.close()
print ("Lines removed:", emptyline)
    
