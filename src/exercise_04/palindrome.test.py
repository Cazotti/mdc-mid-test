import unittest

from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
  def setUp(self):
    self.palindrome = Palindrome()

  def test_is_palindrome_true(self):
    self.assertTrue(self.palindrome.is_palindrome('racecar'))
    self.assertTrue(self.palindrome.is_palindrome('Murder for a jar of red rum'))
    self.assertTrue(self.palindrome.is_palindrome('Evil olive'))

  def test_is_palindrome_false(self):
    self.assertFalse(self.palindrome.is_palindrome('hello'))
    self.assertFalse(self.palindrome.is_palindrome('python'))
    self.assertFalse(self.palindrome.is_palindrome('darkness'))

  def test_check_and_display_palindrome(self):
    result = self.palindrome.check_and_display('racecar')
    self.assertEqual(result, 'racecar is a palindrome!')

  def test_check_and_display_not_palindrome(self):
    result = self.palindrome.check_and_display('oppenheimer')
    self.assertEqual(result, 'oppenheimer is not a palindrome.')

if __name__ == '__main__':
  unittest.main()
