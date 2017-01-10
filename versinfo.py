# import local modules
import functionssheet as f
import imp

# define variable for imported module
p = imp.load_source('versinfo_page', './pages/versinfo_page.py')

# print current page
print p.versinfo_page
print "enter a command: ",
userinput = raw_input()

# call command line function giving the the user input as arg1
f.command(userinput)
