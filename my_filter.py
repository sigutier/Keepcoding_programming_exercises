def is_high_probability(probability):
    """
    Recibe una probabilidad (número entre 0 y 1.0) y devuelve
    True si dicha probabilidad está en el rango correcto y es alta (mayor o igual a 0.8)
    """
    if probability > 1 or probability < 0:
        result = False
    else:
        result = (probability >= 0.8)
    return result

def my_filter_for(elements, predicate):
    """
    Recibe una lista y un predicado. Devuelve otra lista con aquellos elementos
    que superan el test de la funcion predicado.
    """
    accum = []
    for element in elements:
        if predicate(element) == True:
            accum.append(element)
    return accum

print(my_filter_for([0.8, 0.1, 0.2, 0.9, 1.1], is_high_probability))
print(my_filter_for([0.8, 0.1, 0.2, 0.9, 1.1], lambda x: x > 0))

def my_filter_while(elements, predicate):
    accum = []
    i = 0
    while i < len(elements):
        element = elements[i]
        if predicate(element):
            accum.append(element)
        i+=1
    return accum

print(my_filter_while([0.8, 0.1, 0.2, 0.9, 1.1], is_high_probability))

########## FILTER & REDUCE ##########
from my_reduce import my_reduce, sum
from my_map import is_even

numbers = [1,2,3,4,5,6,7,8,9,11,12,14,19,12]

# EVEN NUMBERS
even = my_filter_for(numbers, lambda x: is_even(x))
print("Even numbers:", even)

total_even_numbers = my_reduce(even, 0, sum)
print("Total even numbers:", total_even_numbers)

# UNEVEN NUMBERS
uneven = my_filter_while(numbers, lambda x: not is_even(x))
print("Uneven numbers:", uneven)

total_uneven_numbers = my_reduce(uneven, 0, sum)
print("Total uneven numbers:", total_uneven_numbers)


"""
Te contrataron en un banco como Data Analyst y tu primer trabajo es recibir una lista (larguísima) que contiene la probabilidad, 
calculada mediante un modelo de ML, de que un cliente deje de pagar su hipoteca.
Tu trabajo es quitarle esos muertos al banco, eliminando de la lista los que tengan una probabilidad inferior a un valor que te pasan.
"""
import random

# lista de probabilidades (usando "list comprehensions")
probs = [random.random() for i in range(100)]

def remove_bad_customers(probabilities, threshold):
    """ Recibe una lista de probabilidades de pago y un límite (threshold).
    Debe devolver una nueva lista con aquellas probabilidades que son iguales
    o mayores al threshold. """
    return my_filter_for(probabilities, lambda x: x >= threshold)

print(remove_bad_customers(probs, 0.7))

#########################################
def is_extreme(bmi):
    return bmi < 15 or bmi > 40

def extreme_bmis(list_of_bmis):
    """ Recibe una lista y devuelve otra lista con los valores de bmi que se consideran
    sospechosos de ser un error por extremos (menor que 15 o mayor que 40) """
    return my_filter_for(list_of_bmis, is_extreme)

#########################################
def lists_only(elements):
    """ Filtrar lo que no sea una lista. """
    return my_filter_for(elements, lambda x: type(x) == list)

print(lists_only([34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50']))

def non_empty_lists(elements):
    """ Usando la función lists_only, crea una función non_empty_lists que devuelve una lista 
    con aquellos elementos que son listas y que además NO están vacías. """
    return my_filter_for(elements, lambda x: (type(x) == list) and (len(x) > 0))

print(non_empty_lists([34, 'hola', False, [3,4,5], [None, None], [], ['grijandermoney'], 'EUR50']))
