'''
Exercise 3: Factorial

Write a function to calculate the factorial of a number. Next, create a program that allows the
user to enter a number and displays the corresponding factorial.
'''

class Factorial :
  def calculate_factorial(self, n) :
    return 1 if n == 0 or n == 1 else n * self.calculate_factorial(n - 1)

  def calculate_and_display(self, num) :
    try:
      num = int(num)
      if num < 0:
        return 'Factorial is not defined for negative numbers.'
      result = self.calculate_factorial(num)
      return f'The factorial of {num} is {result}'
    except ValueError:
      return 'Error: Invalid input. Please enter a valid number.'


def main() :
  factorial_calculator = Factorial()
  user_input = input('Enter a number: ')
  result = factorial_calculator.calculate_and_display(user_input)
  print(result)
