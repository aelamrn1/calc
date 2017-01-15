# import modules
import globalvariable as v

# retrieve file object
currentpage = open("pages/helppage.txt", "r")

# define number of dashes
dash = "-" * 87

# assemle page variable
helppage = currentpage.read() % (v.name, v.version, v.name, dash)

# close file
currentpage.close()
