from PyTest import *
for test in _tests('d:\GU\Programming Principles\Workshop\PyTest\W1A3'):
  try:
    ## Print True if the string "cat" and "dog" appear the same number of times  //
    ## in the given string.                                                      //
    ##   "catdog" -> True                                                        //
    ##   "catcat" -> False                                                       //
    ##   "1cat1cadodog" -> True                                                  //
    s = str(input())
    
    while (s.find('cat')!= -1 and s.find('dog')!= -1):
        s = s.lstrip('cat')
        s = s.lstrip('dog')
    if s.find('cat')!= -1 or s.find('dog')!= -1: print(False)
    else: print(True)
    _check()
  except:
    _check(newline = False)
    import sys
    type, obj, tb = sys.exc_info()
    msg = 'Error: ' + str(type)[8:-2] + ' at line ' + str(tb.tb_lineno)
    _prRed(msg)
    _print()
    _logit(msg)
    exit(0)
_logit()
