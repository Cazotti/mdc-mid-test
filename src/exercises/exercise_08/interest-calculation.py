'''
Exercise 8: Interest Calculation

Create a function that calculates the final value of an investment based on initial capital,
interest rate, and investment time (in months). The program must prompt the user for these
values and display the final value.
'''

class InvestmentCalculator:
  @staticmethod
  def calculate_final_value(initial_capital, interest_rate, months):
    final_value = initial_capital * (1 + (interest_rate / 100)) ** months
    return final_value

  def calculate_and_display_final_value(self):
    try:
      initial_capital = float(input('Enter initial capital: '))
      interest_rate = float(input('Enter interest rate (%): '))
      months = int(input('Enter investment time (in months): '))

      final_value = self.calculate_final_value(initial_capital, interest_rate, months)
      print(f'The final value of the investment is: {final_value:.2f}')
    except ValueError:
      print('Error: Invalid input. Please enter valid values.')
