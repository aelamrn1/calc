# import local modules
import globalvariable as v

# retrieve file object
currentpage = open("pages/calcpage.txt", "r")

# define number of dashes
a = "-" * 27

# assemle page variable
calcpage = currentpage.read() % (v.name, v.version, a)

# close file
currentpage.close()
