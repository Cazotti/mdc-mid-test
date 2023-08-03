'''
Exercise 6: Vowel Counter

Create a function that counts the number of vowels in a string. The program should ask the
user for a sentence and display how many vowels it has.
'''

class VowelCounter:
  def count_vowels(self, sentence):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in sentence:
      if char in vowels:
        vowel_count += 1
    return vowel_count

  def count_and_display_vowels(self, sentence):
    vowel_count = self.count_vowels(sentence)
    return f'The sentence has {vowel_count} vowels.'

def main() :
  vowel_counter = VowelCounter()
  sentence = input('Enter a sentence: ')
  result = vowel_counter.count_and_display_vowels(sentence)
  print(result)
