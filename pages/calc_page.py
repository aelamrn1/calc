# import local modules
import globalvariable as v

# retrieve string from plain text file and assign to a variable
with open("pages/calc_page.txt", "r") as currentfile:
    currentpage = currentfile.read()

# define number of dashes
# eventually this will adapt to be as short as longest string in file
a = "-" * 27

# assemble page
calc_page = currentpage % (v.name, v.version, a)
