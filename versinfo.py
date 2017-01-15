# import local modules
import function as f
import globalvariable as v
import imp

# define variable for imported module
p = imp.load_source('versinfopage', './pages/versinfopage.py')

# print current page
print p.versinfopage
print "enter a command"
userinput = raw_input(v.prompt)

# call main function giving the the user input as arg1
f.main(userinput)
