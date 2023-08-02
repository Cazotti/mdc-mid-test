'''
Exercise 4: Palindrome

Create a function that checks whether a word is a palindrome (that is, whether it reads the
same backwards and forwards). The program must ask the user for a word and inform
whether or not it is a palindrome.
'''

class PalindromeChecker:
  def is_palindrome(word):
    word = word.lower().replace(' ', '')
    return word == word[::-1]

  def check_and_display(self, word):
    if self.is_palindrome(word):
      return f'{word} is a palindrome!'
    else:
      return f'{word} is not a palindrome.'

def main() :
  palindrome_checker = PalindromeChecker()
  user_input = input('Enter a word: ')
  result = palindrome_checker.check_and_display(user_input)
  print(result)
