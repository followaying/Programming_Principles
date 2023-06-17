from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if 6 appears as either the first or      //
## last element in the list. The list will be length 1 or more.              //
##    1, 2, 6  -> True                                                       //
##    6, 1, 2, 3  -> True                                                    //
##    3, 2, 1 -> False                                                       //
##/////////////////////////////////////////////////////////////////////////////
n = int(input())
lst = []
for i in range(n): lst.append(int(input()))

#lst = [int(item) for item in input().split()]

if len(lst) == 1:
    if lst[0] == 6: print(True)
    else: print(False)
else: 
    if lst[0] == 6 or lst[-1] == 6:  print(True)
    else: print(False)
