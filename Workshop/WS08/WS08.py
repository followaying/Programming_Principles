import os
os.chdir(r'D:\GU\Programming Principles\Workshop\WS08')

def arithmetic_progression(arr):
    distant = -1
    for i in range(len(arr)-1):
        if distant ==-1: distant = abs(arr[i]-arr[i+1])
        elif abs(arr[i]-arr[i+1]) != distant: return False
    return True

def fever_next(line, lst):
    arr = line.split(' ')
    arr[-1] = (arr[-1])[:-1] #remove \n 
    num = arr[0]
    del arr[0] 
    if "*" in line: 
        if len(arr) == 1: 
            line.remove("*")
            return [line]
        elif len (arr) == 2 or len(arr) ==3: 
            line.remove("*")
            lst+= line.split(' ')
        else:
            for i in range(len(arr)):
                if '*' in arr[i]: 
                    position = i
                    arr[i] = (arr[i])[:-1]
                    break
            if position == len(arr) -1:
                lst += [arr[position], arr[position-1],arr[0]] 
            elif position == 0: 
                lst += [arr[position], arr[position+1], arr[-1]] 
            else: 
                lst += [arr[position], arr[position-1], arr[position+1]]
    else: 
        base = lst.copy()
        for i in range(len(arr)):
            if arr[i] in base: 
                if i == len(arr) -1:
                    if arr[i-1] not in lst: lst.append(arr[i-1])
                    if  arr[0]  not in lst: lst.append(arr[0])
                elif i == 0:
                    if arr[i+1] not in lst: lst.append(arr[i+1])
                    if  arr[i-1]  not in lst: lst.append(arr[i-1])
                else: 
                    if arr[i-1] not in lst: lst.append(arr[i-1])
                    if  arr[i+1]  not in lst: lst.append(arr[i+1])
    return lst, num

def checknumber():
    file1 = open("P5_v1.txt", 'r')
    fever = False
    lst = []
    while True:
        line = file1.readline()
        if line =="": break
        if '*' not in line and fever != True: continue
        elif '*' in line:  
            fever  = True
        lst,num = fever_next(line,lst)
        print(num, end = " ")
        print (*lst, sep = " ", end = " ")
        print(len(lst))
        
    file1.close()
    
checknumber()