import sys
import string

def main() :
    arguments = sys.argv

    if len(arguments) == 1:
        start = input("What is the text to count?\n")
    elif len(arguments) > 1 :
        start = arguments[1:]

    majuscule = numeric = minuscule = count = ponct = space = 0
    ponctuation = string.punctuation
    for i in start:
        for y in i:
            if y.isupper() :
                majuscule += 1
            elif y.isnumeric() :
                numeric += 1
            elif y.islower() :
                minuscule += 1
            elif y in ponctuation:
                ponct += 1
            elif y.isspace():
                space += 1
            count +=1

    print(f"The text contains {count} characters:\n{majuscule} upper letters\n{minuscule} lower letters")
    print(f"{ponct} punctuation marks\n{space} spaces\n{numeric} digits")

main()