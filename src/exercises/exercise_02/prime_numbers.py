'''
Exercise 2: Prime Numbers

Write a function that checks whether a number is prime or not. Then create a program that
prints the first 10 prime numbers.
'''

class PrimeNumber :
  def is_prime(self, number):
    if number <= 1 :
      return False
    if number <= 3 :
      return True
    if number % 2 == 0 or number % 3 == 0:
      return False
    i = 5
    while i * i <= number :
      if number % i == 0 or number % (i + 2) == 0:
        return False
      i += 6
    return True

  def get_first_n_primes(self, n) :
    count = 0
    num = 2
    n_primes = []
    while count < n :
      if self.is_prime(num) :
        n_primes.append(num)
        count += 1
      num += 1
    return n_primes

  def generate_and_print_primes(self, n) :
    primes = self.get_first_n_primes(n)
    print('First', n, 'prime numbers:', primes)
