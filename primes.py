"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list=[]
    counter = 0
    primenumber = 2;

    while(counter<number_of_primes):
        primeCheck = True

        for i in range(2,primenumber):
            if(primenumber % i ==0):
                primeCheck=False

        if primeCheck:
            list.append(primenumber)
            counter += counter
        primenumber+=primenumber

    return list
