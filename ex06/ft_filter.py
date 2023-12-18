def ft_filter(function, elements):
    """Allows you to process an iterable and extract those items that satisfy a given condition

    Args:
        function (function or None): function allow to check
        elements (iterable): elements to check

    Returns:
        list[str]: Return an iterator yielding those items of iterable for which function(item) is true.
        If function is None, return the items that are true.
    """
    if function is not None:
        return [element for element in elements if function(element)] #add the result of the function in a list only if i satisfy function
    return [element for element in elements] #return all in a list if function is None
