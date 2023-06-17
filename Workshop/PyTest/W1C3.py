from PyTest import *
##///////////////////// PROBLEM STATEMENT /////////////////////
## Given an int list, print True if it contains a 2 or a 3.  //
##    2, 5  -> True                                          //
##    4, 3  -> True                                          //
##    4, 5  -> False                                         //
##/////////////////////////////////////////////////////////////
lst=[]
lst = [int(item) for item in input().split()]
print (len(lst))
if lst.index(2) >=0 or lst.index(3) >=0: print(True)
else: print(False)
a=(1,2,3,4,5,6,7)

len(a)