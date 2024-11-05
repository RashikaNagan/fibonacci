'''def fibonacci(n):
    sum = 0
    firstnr = 1
    secondnr = 1
    print(firstnr)
    print(secondnr)
    for i in range(n-2):
        thirdnr = firstnr + secondnr
        firstnr = secondnr
        secondnr = thirdnr
        print(secondnr)
    
    
fibonacci(5)'''

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) #call the function here
    
print(fibonacci(8))


    