import unittest

from prime_numbers import PrimeNumber

class TestPrimeNumber(unittest.TestCase):
  def setUp(self):
    self.prime_generator = PrimeNumber()

  def test_is_prime(self):
    self.assertFalse(self.prime_generator.is_prime(0))
    self.assertFalse(self.prime_generator.is_prime(1))
    self.assertTrue(self.prime_generator.is_prime(2))
    self.assertTrue(self.prime_generator.is_prime(3))
    self.assertFalse(self.prime_generator.is_prime(4))
    self.assertTrue(self.prime_generator.is_prime(5))
    self.assertTrue(self.prime_generator.is_prime(17))
    self.assertFalse(self.prime_generator.is_prime(20))

  def test_get_first_n_primes(self):
    self.assertEqual(self.prime_generator.get_first_n_primes(0), [])
    self.assertEqual(self.prime_generator.get_first_n_primes(1), [2])
    self.assertEqual(self.prime_generator.get_first_n_primes(5), [2, 3, 5, 7, 11])
    self.assertEqual(self.prime_generator.get_first_n_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

if __name__ == '__main__':
  unittest.main()
