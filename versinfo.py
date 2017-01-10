# import local modules
import functionssheet as f
import globalvariable as v
import imp

# define variable for imported module
p = imp.load_source('versinfo_page', './pages/versinfo_page.py')

# print current page
print p.versinfo_page
print "enter a command"
userinput = raw_input(v.prompt)

# call command line function giving the the user input as arg1
f.command(userinput)
