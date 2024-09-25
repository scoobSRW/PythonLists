grades = [85, 90, 78, 88, 76,
          95, 89, 80, 72, 93]

grades_in_order = sorted(grades, reverse=True)
print(grades_in_order)

grade_avrg = sum(grades) / len(grades)
print(grade_avrg)
