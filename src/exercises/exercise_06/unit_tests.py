import unittest
from vowel_counter import VowelCounter

class TestVowelCounter(unittest.TestCase):
  def setUp(self):
    self.vowel_counter = VowelCounter()

  def test_count_vowels(self):
    self.assertEqual(self.vowel_counter.count_vowels('Hello'), 2)
    self.assertEqual(self.vowel_counter.count_vowels('Python is awesome'), 6)
    self.assertEqual(self.vowel_counter.count_vowels('AEIOUaeiou'), 10)
    self.assertEqual(self.vowel_counter.count_vowels(''), 0)

  def test_count_and_display_vowels(self):
    result = self.vowel_counter.count_and_display_vowels('Hello, how are you?')
    self.assertEqual(result, 'The sentence has 7 vowels.')

    result = self.vowel_counter.count_and_display_vowels('Python is fun!')
    self.assertEqual(result, 'The sentence has 3 vowels.')

  def test_count_and_display_vowels_empty(self):
    result = self.vowel_counter.count_and_display_vowels('')
    self.assertEqual(result, 'The sentence has 0 vowels.')

if __name__ == '__main__':
  unittest.main()
