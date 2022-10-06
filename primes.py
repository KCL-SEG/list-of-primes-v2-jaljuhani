"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def primes(number_of_primes):
    list = []
    count = 0;
    primenumber = 2;
    if(number_of_primes<=0):
        raise ValueError("Use a positve number greater than 0 ")

    else:
        while (count < number_of_primes):
            primeCheck = True

            for i in range(2, primenumber):
                if (primenumber % i == 0):
                    primeCheck = False

            if primeCheck:
                list.append(primenumber)
                count += 1
            primenumber += 1


        return list
