# import modules
import globalvariable as v

# retrieve string from plain text file and assign to a variable
with open("pages/help_page.txt", "r") as currentfile:
    currentpage = currentfile.read()

# define number of dashes
# eventually this will adapt to be as short as longest string in file
dash = "-" * 87

# assemble page
help_page = currentpage % (v.name, v.version, dash)
