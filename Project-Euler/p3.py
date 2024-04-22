'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
from math import sqrt, ceil
def isPrime(num):

    if num < 2:
        return False
    else:
        for i in range(2, ceil(sqrt(num))):
            if not num % i: return False
    return True
        
def primeFactorize(num):
    factors = []
    divisor = 2

    while num > 1:
        if isPrime(divisor):
            if num % divisor == 0:
                factors.append(divisor)
                num = num / divisor
            else: divisor += 1        
        else: divisor += 1
    return factors

def main():
    factors = primeFactorize(600851475143)
    print(factors[-1])

if __name__ == "__main__" : main()
