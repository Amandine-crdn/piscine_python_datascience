def all_thing_is_obj(object: any ) -> int:

    type_object = type(object)
    if type(object) == list :
        print(f"List : {type_object}")
    elif type(object) == tuple :
        print(f"Tuple : {type_object}")
    elif type(object) == set :
        print(f"Set : {type_object}")
    elif type(object) == dict :
        print(f"Dict : {type_object}")
    elif type(object) == str :
        print(f"Brian is in the kitchen : {type_object}")
    else :
        print("Type not found")
    return 42