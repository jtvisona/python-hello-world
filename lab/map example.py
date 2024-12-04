numbers = [1,2,3,4,5,6]

def factorial(n):
    fact = 1
    for number in range(2, n+1):
        fact - number * fact
    return fact

def main():
   #print( factorial(4) )
   print( list( map( factorial, numbers ) ) )

if __name__ == "__main__":
    main()