def length_for(seq):
    index = 0
    for element in seq:
        index += 1
    return index

def length_while(seq):
    index = 0
    while seq[index:]:
        index += 1
    return index

def is_member_for(needle, seq):
    found = False
    for element in seq:
        if element == needle:
            found = True
            break
    return found

def is_member_while(needle, seq):
    found = False
    index = 0
    while seq[index:]:
        if seq[index] == needle:
            found = True
            break
        index += 1
    return found

def is_not_member(needle, seq):
    return not is_member_for(needle, seq)

def how_many_for(needle, seq):
    count = 0
    for element in seq:
        if element == needle:
            count += 1
    return count

def how_many_while(needle, seq):
    count = 0
    index = 0
    while seq[index:]:
        if seq[index] == needle:
            count += 1
        index += 1
    return count

def sum_all_for(seq):
    sum = 0
    for number in seq:
        sum += number
    return sum

def sum_all_while(seq):
    sum = 0
    index = 0
    while seq[index:]:
        sum += seq[index]
        index += 1
    return sum

def multiply_all_for(seq):
    product = 1
    for number in seq:
        product = product * number
    return product

def multiply_all_while(seq):
    product = 1
    index = 0
    while seq[index:]:
        product = product * seq[index]
        index += 1
    return product

def concat_all(seq):
    """ Podemos usar el bucle for para obtener una sola cadena de la lista. 
    En este método, iteramos sobre todos los valores y luego agregamos cada valor a una cadena vacía. """
    concat = ""
    for element in seq:
        concat += str(element) + " "
    return concat

def concat_all_join(seq):
    """ El método join() devuelve una cadena en la que el separador de cadenas("separador".join(list)) une la secuencia de elementos. """
    return (" ".join(seq))

def and_all(seq):
    is_all_true = True
    if len(seq) == 0:
        return None
    for element in seq:
        if element == False:
            is_all_true = False
            break
    return is_all_true


lst = ["hola", 5, 8, "a", True, False, 8, {"hola":"adios"}]
numbers = [1,2,3,4]
str_lst = ['hello', 'world']
bool_lst = [True and (False or True) and (not (False or True))]

print(length_for(lst)) 
print(length_while(lst))
print(is_member_for(10, lst))
print(is_member_while(10, lst))
print(is_not_member(10, lst))
print(how_many_for(8, lst))
print(how_many_while(8, lst))
print(sum_all_for(numbers))
print(sum_all_while(numbers))
print(multiply_all_for(numbers))
print(multiply_all_while(numbers))
print(concat_all(str_lst))
print(concat_all_join(str_lst))
print(and_all(bool_lst))
