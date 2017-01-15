# import modules
import globalvariable as v

# retrieve file object
currentpage = open("pages/versinfopage.txt", "r")

# define number of dashes
dash = "-" * 24

# assemle page variable
versinfopage = currentpage.read() % (v.name, v.version, v.name, v.version,
                                     v.creator, dash)

# close file
currentpage.close()
