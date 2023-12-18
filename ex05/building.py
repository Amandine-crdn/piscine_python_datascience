import sys
import string

def main() :

    try:
        #on récupère les arguments
        arguments = sys.argv

        #si l'input est dans l'argument d'éxecution on le récupère
        if len(arguments) > 1 :
            user_input = arguments[1:]
        else: #sinon on demande une rentrée valide d'input
            user_input = input("What is the text to count?\n")
            while not user_input.strip(" "):  #on vérifie si la saisie n'est pas vide après la suppression des espaces
                print("Please enter some text.")
                user_input = input("What is the text to count?\n")
        
        majuscule = numeric = minuscule = count = ponct = space = 0
        ponctuation = string.punctuation
        for i in user_input:
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
    
    except KeyboardInterrupt:
        print("\nProgram interrupted by user (Ctrl+C). Exiting.")


if __name__ == "__main__":
    main()