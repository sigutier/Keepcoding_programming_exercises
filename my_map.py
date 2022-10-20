def convert(prices, rate):
    """
    Crea una función que recibe una lista de precios en dólares, y devuelve esos mismos 
    precios en otra divisa. Para ello, también recibe una tasa de conversión
    """
    new_prices = []
    for price in prices:
        new_prices.append(price * rate)
    return new_prices

print(convert([1,2,3,4], 1.1))

def convert_if_big(prices, rate):
    """
    Crea una función que recibe la misma lista de precios en dólares y 
    sólo convierte a otra divisa los que sean mayores que 10.
    """
    new_prices = []
    for price in prices:
        new_price = price
        if price > 10:
            new_price = price * rate
        new_prices.append(new_price)
    return new_prices

print(convert_if_big([1, 34, 10, 12], 2.5))

def to_euro_string(prices):
    """
    Crea una función que recibe una lista de números con precios en euros y devuelve una 
    lista de cadenas. Cada precio debe de ser convertido en una cadena con el estandar ISO para €: 458 -> 'EUR 45'.
    """
    lista_iso = []
    for element in prices:
        lista_iso.append('EUR ' + str(element))
    return lista_iso

print(to_euro_string([34, 24.6, 0.55]))

def my_map(seq, transformer):
    """ Función 'map' transforma cada elemento de la lista original en uno nuevo """
    new_seq = []
    for element in seq:
        new_seq.append(transformer(element))
    return new_seq

print("map int:", my_map([1,2,3,4], lambda x: x + 1))
print("map str:", my_map([1,2,3,4], lambda x: str(x)))

"""
Si queremos transformar aquellos elementos que cumplan una condición,
usamos un predicado (función que devuelve un booleano) dentro del transformer.
Por ejemplo, si queremos duplicar aquellos números que sean pares: 
"""
def is_even(n):
    return n % 2 == 0   # devuelve True si es par

def dupl_if_even(n):
    if is_even(n):
        return n * 2   # si n es par, multiplicarlo por 2
    else:
        return n       # si no, devolver n sin modificar

print("even * 2:", my_map([1,2,3,4,5,6,7,8], dupl_if_even))

def stringify(items):
    """
    Usando 'map', define la función stringify, que recibe una lista de cosas, y devuelve una lista de esas cosas convertidas en cadenas. Por ejemplo:
    [1, 4, True, None] ---> ['1', '4', 'True', 'None']
    """
    return my_map(items, lambda x: str(x))

print(stringify([1, 4, True, None]))

def ucase(items):
    """ Usando 'map', crea una función 'ucase' que recibe una lista de cadenas y devuelve una lista de cadenas, todas en mayúsculas """
    return my_map(items, lambda x: x.upper())

print(ucase(['Hello', 'worLd']))

def to_positive(numbers):
    """
    Usando `map`, crea la función `to_positive` que recibe una lista de números positivos y negativos, y devuelve una lista con los valores absolutos de dichos números.
    [1, 0, -3, -5, 7] ----------> [1, 0, 3, 5, 7]
    """
    return my_map(numbers, lambda number: abs(number))

print("Absolute value list:", to_positive([5, -6, 7, -8, -10]))

def dollar_only(prices):
    """
    Usando map crea la función dollar_only. Recibe una lista de valores en diferentes divisas (usando el estandar ISO), tales como:
    'CHF 12' Doce francos suizos
    'USD 22' Veintidós dólares
    'EUR 60' 60 euros
    Devuelve una lista, de igual longitud, donde sólo aparezcan los valores que estaban en dólares. Los demás se sustituyen por la cadena vacía:
    ['CHF 23', 'EUR 87', 'USD 2', 'USD 21', 'BTC 3'] ---> ['', '', 'USD 2', 'USD 21', '']
    """
    return my_map(prices, lambda x: x if 'USD' in x else '')

print(dollar_only(['CHF 23', 'EUR 87', 'USD 2', 'USD 21', 'BTC 3']))

def lens(list_of_lists):
    """ Usando 'map' crea la función 'lens'. 'lens' recibe una lista de listas y devuelve una lista con las longitudes de dichas listas. """
    return my_map(list_of_lists, lambda list: len(list))

lista_de_listas = [['hello', 'world'], [''], [None], [True, False], [0,1,2,3], []]

print("Length of each list:", lens(lista_de_listas))

# Utilizando directamente 'map' y 'len':
print("Longitud de cada lista:", my_map(lista_de_listas, len))
