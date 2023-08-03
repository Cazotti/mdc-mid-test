'''
Exercise 7: Grade Average

Create a program that takes a student's grades in three different subjects and calculates the
average of the grades. Then display the calculated average.
'''

class GradeAverage:
  @staticmethod
  def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

  def get_and_display_average(self):
    try:
      grades = []
      for i in range(3):
        grade = float(input(f"Enter grade for subject {i+1}: "))
        grades.append(grade)

      average = self.calculate_average(grades)
      print(f"The average grade is: {average:.2f}")
    except ValueError:
      print("Error: Invalid input. Please enter valid grades.")
