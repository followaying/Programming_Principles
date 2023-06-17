from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, print True if either of the strings appears at the     //
## very end of the other string, ignoring upper/lower case differences       //
## (in other words, the computation should not be "case sensitive").         //
##   "Hiabc", "abc" -> True                                                  //
##   "AbC", "HiaBc" -> True                                                  //
##   "abc", "abXabc" -> True                                                 //
##   "abc", "abXaXc" -> False                                                //
##/////////////////////////////////////////////////////////////////////////////

s1 = str(input())
s2 = str(input())
s1 = s1.upper()
s2 = s2.upper()

if len(s1) > len(s2):
    if s1.find(s2) ==len(s1) - len(s2): print(True)
    else: print(False)
else:
    if s2.find(s1) ==len(s2) - len(s1): print(True)
    else: print(False)
