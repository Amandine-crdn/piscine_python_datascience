def ft_filter(function, element) :
    new_list = [i for i in element if function(i)]
    return new_list