def factorial(n):
    result=n
    for i in  range(1,n):
        result*=1
    return result

print(factorial(10))

def factorialb(n):
    if n==1:
        return 1
    else:
        return n*factorialb(n-1)
print(factorialb(3))

def power(x,n):
    result=1
    for i in range(n):
        result*=x
    return  result
print(power(2,6))

def powerb(x,n):
    if n==0:
        return 1
    else:
        return x*powerb(x,n-1)
print(powerb(2,4))

def search(sequence,number,lower,upper):
    if lower==upper:
        assert number==sequence[upper]
        return upper
    else:
        middle=(lower+power)//2
        if number> sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return  search(sequence,number,lower,middle)
seq=[34,67,8,123,4,100,95]
seq.sort()
print(seq)
print(seq[1])
print(len(seq))
search(seq,9,)





