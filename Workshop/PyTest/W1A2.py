from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if "bad" appears starting at index 0 or 1 in   //
## the string, such as with "badxxx" or  "xbadxx" but not "xxbadxx". The     //
## string may be any length, including 0.                                    //
##   "badxx" -> True                                                         //
##   "xbadxx" -> True                                                        //
##   "xxbadxx" -> False                                                      //
##/////////////////////////////////////////////////////////////////////////////

s= str(input())
if s.find('bad') == 0 or s.find('bad') == 1: print(True)
else: print(False) 
