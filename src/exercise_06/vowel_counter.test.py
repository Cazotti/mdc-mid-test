import unittest

from vowel_counter import VowelCounter

class TestVowelCounter(unittest.TestCase):
  def setUp(self):
    self.vowel_counter = VowelCounter()

  def test_count_vowels(self):
    self.assertEqual(self.vowel_counter.count_vowels(''), 0)
    self.assertEqual(self.vowel_counter.count_vowels('AEIOUaeiou'), 10)
    self.assertEqual(self.vowel_counter.count_vowels('Darkness'), 2)
    self.assertEqual(self.vowel_counter.count_vowels('A nut for a jar of tuna'), 8)

  def test_count_and_display_vowels(self):
    result = self.vowel_counter.count_and_display_vowels('We are going on holiday tomorrow')
    self.assertEqual(result, 'The sentence has 12 vowels.')

    result = self.vowel_counter.count_and_display_vowels('I phoned her but she was not there.')
    self.assertEqual(result, 'The sentence has 10 vowels.')

  def test_count_and_display_vowels_empty(self):
    result = self.vowel_counter.count_and_display_vowels('')
    self.assertEqual(result, 'The sentence has 0 vowels.')

if __name__ == '__main__':
  unittest.main()
