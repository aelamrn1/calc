# import modules
import globalvariable as v

# retrieve string from plain text file and assign to a variable
with open("pages/versinfo_page.txt", "r") as currentfile:
    currentpage = currentfile.read()

# define number of dashes
# eventually this will adapt to be as short as longest string in file
dash = "-" * 24

# assemble page
versinfo_page = currentpage % (v.name, v.version, v.name, v.version, v.creator,
                               dash)
