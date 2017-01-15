# import standard libraries
import os

# import local modules
import globalvariable as v
from random import randint

w = open("worksheet.txt", "r+")

# define arg1 line function
def main(arg1):
    # check for unknown arg1s
    while arg1 not in ("calc", "help", "version info", "RN", "AC",
                       "/", "*", "-", "+", "=", "quit"):
        print v.ukn
        arg1 = raw_input(v.prompt)
    # check for calc arg1
    if arg1 == "calc":
        os.system("clear")
        os.system("python ./calc.py")
    # check for help arg1
    elif arg1 == "help":
        os.system("clear")
        os.system("python ./help.py")
    # check for version info arg1
    elif arg1 == "version info":
        os.system("clear")
        os.system("python ./versinfo.py")
    # check for version info arg1
    elif arg1 == "quit":
        quit()
    # clear current answer
    elif arg1 == "AC":
        v.result = 0
        print v.prompttext; i = raw_input(v.prompt)
        main(i)
    # check for random integer arg1
    elif arg1 == "RN":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        rnd(rn1, rn2)
    # check for division arg1
    elif arg1 == "/":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        div(rn1, rn2)
    # check for multiplication arg1
    elif arg1 == "*":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        mul(rn1, rn2)
    # check for subtraction arg1
    elif arg1 == "-":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        sub(rn1, rn2)
    # check for addition arg1
    elif arg1 == "+":
        print "give your first number: "
        rn1 = input(v.prompt)
        print "give your second number: "
        rn2 = input(v.prompt)
        add(rn1, rn2)
    # check for show answer arg1
    elif arg1 == "=":
        equ()


# define random integer function
def rnd(arg1, arg2):
    v.result = randint(arg1, arg2)
    print v.prompttext
    i = raw_input(v.prompt)
    main(i)


# define divide function
def div(arg1, arg2):
    v.result = arg1 * 1.0 / arg2
    print v.prompttext
    i = raw_input(v.prompt)
    main(i)


# define multiplication function
def mul(arg1, arg2):
    v.result = arg1 * 1.0 * arg2
    print v.prompttext
    i = raw_input(v.prompt)
    main(i)


# define subtraction function
def sub(arg1, arg2):
    v.result = arg1 * 1.0 - arg2
    print v.prompttext
    i = raw_input(v.prompt)
    main(i)


# define addition function
def add(arg1, arg2):
    v.result = arg1 * 1.0 + arg2
    print v.prompttext
    i = raw_input(v.prompt)
    main(i)


# define show answer function
def equ():
    print("the current answer is: %s") % v.result
    print v.prompttext; i = raw_input(v.prompt)
    main(i)
