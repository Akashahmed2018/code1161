"""Tidy up this file.

This file runs, but it's a mess!
Go through it and change it until there are no more linter errors or warnings.
Make sure that your code still runs without any errors by pressing
[ctrl]+[shift]+[b] as often as you think you need to.
"""
from __future__ import division
from __future__ import print_function
#This will print the words 'hello!Let's get started'
print  ("hello! Let's get started") #It printed the words but had one line above it saying 'none'
#jobs is the variable name, and will print out a list with the words in it.
jobs=['get','this',
'file','to','pass',
  'the','linter'] #a list with the words was printed out.
# The variable will show the words in quotation marks. 
InOtherWords="make it show no linter errors" #shows the words in single quotation marks.abs

import os
#shows 'jobs'
print(jobs)#shows the list of things represented by the variable 'jobs'.
#displays the words 'make it show no linter errors'.
print(InOtherWords) #it printed out make it show no lintel errors without the single quotation marks. 
#displays 1+1<7*0.5 is (1+1)<(7*0.5), which is a relief!
print(1+1,"is smaller than",7*0.5,"is",(1+1)<(7*0.5),", which is a relief!")#displays "2 is smaller than 3.5 is True , which is a relief!""
#establishes usefulFunction as a function.
def usefulFunction () :#unexpected EOF while parsing (<debug input>, line 1)
    print(os.getcwd())#name 'os' is not defined
usefulFunction( )#name 'usefulFunction' is not defined
