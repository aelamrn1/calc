# import local modules
import globalvariable as v

# retrieve file object
currentpage = open("pages/calc_page.txt", "r")


a = "-" * 27

calcpage = currentpage.read() % (v.name, v.version, a)

# close file
currentpage.close()
