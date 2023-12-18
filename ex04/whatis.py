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

if (args[1][0] == '-' and args[1][1:].isdigit() == True):
    odd_or_even(int(args[1]))
else:

    try:
        assert args[1].isdigit() == True, "argument is not an integer"
        assert len >= 2 , "more than one argument is provided"
        odd_or_even(int(args[1]))

    except AssertionError as e:
        print("AssertionError:", e)
