'''
Exercise 3: Factorial

Write a function to calculate the factorial of a number. Next, create a program that allows the
user to enter a number and displays the corresponding factorial.
'''

class Factorial :
  def calculate_factorial(self, n) :
    if n < 0: return None
    factorial = 1
    for i in range(1, n + 1): factorial *= i
    return factorial

  def calculate_and_display(self, num) :
    try:
      num = int(num)
      if num < 0:
        return 'Factorial is not defined for negative numbers.'
      result = self.calculate_factorial(num)
      if result is not None:
        return f'The factorial of {num} is {result}'
      else:
        return f'Error: Unable to calculate factorial for negative number {num}.'
    except ValueError:
      return 'Error: Invalid input. Please enter a valid number.'


def main() :
  factorial_calculator = Factorial()
  user_input = input('Enter a number: ')
  result = factorial_calculator.calculate_and_display(user_input)
  print(result)
