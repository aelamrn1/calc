# import standard libraries
import os

# import local modules
import function as f
import globalvariable as v
import imp
p = imp.load_source('calcpage', './pages/calcpage.py')

# run on startup
os.system("clear")

# print current page
print p.calcpage
print "enter a command"
userinput = raw_input(v.prompt)

# call main function giving the user input as arg1
f.main(userinput)
