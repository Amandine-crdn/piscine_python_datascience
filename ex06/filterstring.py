from ft_filter import ft_filter
import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("AssertionError: the arguments are bad")
    sys.exit(1)
    
isalpha = ft_filter(str.isdigit, arguments[0])
isdigit = ft_filter(str.isalpha, arguments[1])

if isalpha or isdigit:
    print("AssertionError: the arguments are bad")

tableau = []
if len(arguments[0]) > int(arguments[1]):
    tableau = arguments[0].split(' ')

print(tableau)