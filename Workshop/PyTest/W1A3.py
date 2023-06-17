from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print True if the string "cat" and "dog" appear the same number of times  //
## in the given string.                                                      //
##   "catdog" -> True                                                        //
##   "catcat" -> False                                                       //
##   "1cat1cadodog" -> True                                                  //
##/////////////////////////////////////////////////////////////////////////////
s = str(input())

while (s.find('cat')!= -1 and s.find('dog')!= -1):
    s = s.lstrip('cat')
    s = s.lstrip('dog')
if s.find('cat')!= -1 or s.find('dog')!= -1: print(False)
else: print(True)