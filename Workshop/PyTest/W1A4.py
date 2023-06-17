from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the  concatenation creates a double-char,   //
## then omit one of the chars, so "abc" and "cat" yields "abcat".            //
##   "abc", "cat" -> "abcat"                                                 //
##   "dog", "cat" -> "dogcat"                                                //
##   "abc", "" -> "abc"                                                      //
##/////////////////////////////////////////////////////////////////////////////
s1= str(input())
s2= str(input())
if s1[-1] == s2[0]: print(s1[:-1] + s2)
else: print(s1+s2)