def fibs(n):
    if n<=2:
        return [1]*(n+1)
    fs= fibs(n-1)
    return (fibs(n-1).append(fib(n)))
print (fibs(15))

#print (fibs(15))
