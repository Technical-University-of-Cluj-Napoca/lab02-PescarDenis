def multiply_all(*args : int) -> int :
    res = 1
    for arg in args :
        res *= arg
    return res
 
#print(multiply_all(1,2,3,4,5))
#print(multiply_all())
#print(multiply_all(7))