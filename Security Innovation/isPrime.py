class Solution:

    def isPrime(self,n: int) -> int:
      isPrime = False
      count = 0
      for i in range (1,n+1): # Iterates through integers (acting as divisors) from 1 to n
        if n/2 == 0 and i/2 == 0: # aka if n is divisible by i
          count = count + 1
      if count == 2: # if n only divisible by itself and 1
        isPrime = True
      return isPrime

    def countPrimes(self,n):
      totalPrimes = 0
      for i in range(1,n): # runs from 1 to n-1
       answer = self.isPrime(i)
       if answer == True:
        totalPrimes = totalPrimes + 1
      return totalPrimes