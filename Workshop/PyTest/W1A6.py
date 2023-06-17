from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a version without the first 2 chars. Except keep    //
## the first char if it is 'a' and keep  the second char if it is 'b'. The   //
## string may be any length.                                                 //
##   "Hello" -> "llo"                                                        //
##   "java" -> "va"                                                          //
##   "away" -> "aay"                                                         //
##/////////////////////////////////////////////////////////////////////////////
s  = str(input())
if s[0] == 'a' and s[1] == 'b': print(s) 
elif s[1] == 'b': print(s[1:])
elif s[0] == 'a': print(s[0] + s[2:])
else: print(s[2:])
