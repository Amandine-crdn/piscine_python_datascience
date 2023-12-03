import sys

def odd_or_even(to_find):
    if to_find % 2 == 0 :
        print("I'm Even.")
    elif to_find % 2 != 0 :
        print("I'm Odd.")

args = sys.argv
len = len(args)

if len == 1:
    sys.exit(1)

if len != 2:
    print("AssertionError: more than one argument is provided")
elif (args[1][0] == '-' and args[1][1:].isdigit() == True):
    odd_or_even(int(args[1]))
elif (args[1].isdigit() == False) :
    print("AssertionError: argument is not an integer")
else:
    odd_or_even(int(args[1]))