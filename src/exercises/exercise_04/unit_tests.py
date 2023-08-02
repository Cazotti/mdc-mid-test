import unittest

from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
  def setUp(self):
    self.palindrome = Palindrome()

  def test_is_palindrome_true(self):
    self.assertTrue(self.palindrome.is_palindrome('racecar'))
    self.assertTrue(self.palindrome.is_palindrome('A man a plan a canal Panama'))
    self.assertTrue(self.palindrome.is_palindrome('madam'))

  def test_is_palindrome_false(self):
    self.assertFalse(self.palindrome.is_palindrome('hello'))
    self.assertFalse(self.palindrome.is_palindrome('python'))

  def test_check_and_display_palindrome(self):
    result = self.palindrome.check_and_display('racecar')
    self.assertEqual(result, 'racecar is a palindrome!')

  def test_check_and_display_not_palindrome(self):
    result = self.palindrome.check_and_display('hello')
    self.assertEqual(result, 'hello is not a palindrome.')

if __name__ == '__main__':
  unittest.main()
