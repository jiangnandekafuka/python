def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print fibs(100)

def square(x):
    'Calculates the square of the number x.'
    return x*x
print square(7)
print square.__doc__
