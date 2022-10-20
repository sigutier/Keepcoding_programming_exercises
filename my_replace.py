def my_replace(elements, predicate, new_value):
    new_list = []
    for element in elements:
        if predicate(element):
            new_list.append(new_value)
        else:
            new_list.append(element)
    return new_list
