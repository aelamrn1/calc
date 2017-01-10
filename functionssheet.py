# import standard libraries
import os

# import local modules
import globalvariable as v
from random import randint


# define command line function
def command(arg1):
    # check for unknown commands
    while arg1 not in ("calc", "help", "version info", "RN", "AC",
                       "/", "*", "-", "+", "="):
        print v.ukn
        arg1 = raw_input(v.prompt)
    # check for calc command
    if arg1 == "calc":
        os.system("clear")
        os.system("python ./calc.py")
    # check for help command
    elif arg1 == "help":
        os.system("clear")
        os.system("python ./help.py")
    # check for version info command
    elif arg1 == "version info":
        os.system("clear")
        os.system("python ./versinfo.py")
    # check for random integer command
    elif arg1 == "RN":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        rnd(rn1, rn2)
    # check for division command
    elif arg1 == "/":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        div(rn1, rn2)
    # check for multiplication command
    elif arg1 == "*":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        mul(rn1, rn2)
    # check for subtraction command
    elif arg1 == "-":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        sub(rn1, rn2)
    # check for addition command
    elif arg1 == "+":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        add(rn1, rn2)
    # check for show answer command
    elif arg1 == "=":
        equ()


# define random integer function
def rnd(arg1, arg2):
    v.result = randint(arg1, arg2)
    print v.prompttext
    i = raw_input(v.prompt)
    command(i)


# define divide function
def div(arg1, arg2):
    v.result = arg1 * 1.0 / arg2
    print v.prompttext
    i = raw_input(v.prompt)
    command(i)


# define multiplication function
def mul(arg1, arg2):
    v.result = arg1 * 1.0 * arg2
    print v.prompttext
    i = raw_input(v.prompt)
    command(i)


# define subtraction function
def sub(arg1, arg2):
    v.result = arg1 * 1.0 - arg2
    print v.prompttext
    i = raw_input(v.prompt)
    command(i)


# define addition function
def add(arg1, arg2):
    v.result = arg1 * 1.0 + arg2
    print v.prompttext
    i = raw_input(v.prompt)
    command(i)


# define show answer function
def equ():
    print("the current answer is: %r") % v.result
    print v.prompttext; i = raw_input(v.prompt)
    command(i)
