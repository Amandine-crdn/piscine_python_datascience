ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

#Modification par indice :
ft_list[1] = "Word"

#objet immuable => convertir en list
ft_tuple = list(ft_tuple)
del ft_tuple[1]
ft_tuple.append("France")

#supprimer et ajouter
ft_set.remove("Hello")
ft_set.add("Paris")

#Modification par clé :
ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)