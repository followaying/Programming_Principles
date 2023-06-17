from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the strings are different lengths, omit     //
## chars from the longer string so it is the same length as the shorter      //
## string. So "Hello" and "Hi" yield "loHi". The strings may be any length.  //
##                                                                           //
##   "Hello", "Hi" -> "loHi"                                                 //
##   "Hello", "java" -> "ellojava"                                           //
##   "java", "Hello" -> "javaello"                                           //
##/////////////////////////////////////////////////////////////////////////////

s1 = str(input())
s2 = str(input())

if len(s1) > len(s2): print(s1[-len(s2):] + s2)
elif len(s1) < len(s2): print(s1+ s2[-len(s1):])
else: print(s1+s2)
