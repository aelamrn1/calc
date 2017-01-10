# import standard libraries
import os

# import local modules
import functionssheet as f
import imp

# define variable for imported module
p = imp.load_source('calc_page', './pages/calc_page.py')

# run on startup
os.system("clear")

# print current page
print p.calc_page
print "enter a command: ",
userinput = raw_input()

# call command line function giving the the user input as arg1
f.command(userinput)
