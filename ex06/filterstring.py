from ft_filter import ft_filter
import sys
import string

def main():

    try:
        arguments = sys.argv[1:]

        #Excepts
        ponctuation = string.punctuation
        for characters in arguments[0]:
            assert characters not in ponctuation, "punctuation character found"
        assert len(arguments) == 2 , "the arguments are bad"
        int(arguments[1]) #si ce n'est pas un int return une ValueError
        
        tableau = arguments[0].split(' ') #je veux une liste de mot sans espace
        new_tableau = list(ft_filter(lambda x:len(x) > int(arguments[1]), tableau)) #je selectionne avec la lambda
        print(new_tableau)

    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except TypeError as e:
        print(e)       

if __name__ == "__main__":
    main()
    
#ZeroDivisionError, NameError et TypeError. KeyboardInterrupt. (RuntimeError
# raise Exception OSError ValueError  (AttributeError)
