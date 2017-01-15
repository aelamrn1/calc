# import local modules
import function as f
import globalvariable as v
import imp

# define variable for imported module
p = imp.load_source('help_page', './pages/helppage.py')

# print current page
print p.helppage
print "enter a command"
userinput = raw_input(v.prompt)

# call main function giving the the user input as arg1
f.main(userinput)
