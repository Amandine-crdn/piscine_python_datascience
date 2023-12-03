ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

#modifier
ft_list[1] = "Word"

#convertir en list
ft_tuple = list(ft_tuple)
#supprimer un element
del ft_tuple[1]
#rajouter un element
ft_tuple.append("France")

#supprimer
ft_set.pop()
#convertir en list
# ft_set.remove()
ft_set = list(ft_set)
ft_set.insert(1, "Paris")

ft_dict["Hello"] = "42Paris"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)