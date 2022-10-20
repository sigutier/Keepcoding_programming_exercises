def my_reduce(seq, initial_value, operation):
    accum = initial_value
    for element in seq:
        accum = operation(accum, element)
    return accum

def sum(a,b):
    return a+b

def product(a,b):
    return a*b

""" nums = [1,2,3,4,5,6]
print("Suma =", my_reduce(nums, 0, sum))
print("Producto =", my_reduce(nums, 1, product))
print(my_reduce(nums, 1, lambda a,b : a*b)) """
