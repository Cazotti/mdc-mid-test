'''
Exercise 5: Table

Create a program that receives a number from the user and displays the table of that
number, from 1 to 10.
'''

class Table:
  def display_multiplication_table(self, number):
    print(f'Multiplication table of {number}:')
    for i in range(1, 11):
      result = number * i
      print(f'{number} x {i} = {result}')

  def generate_and_display_table(self, num):
    try:
      num = int(num)
      self.display_multiplication_table(num)
    except ValueError:
      print('Error: Invalid input. Please enter a valid number.')


def main() :
  table = Table()
  user_input = input('Enter a number: ')
  table.generate_and_display_table(user_input)
