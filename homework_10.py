import numpy as np

import task_1
import task_2
import task_3
import task_4
import task_5
import task_6


def separator(t):
    print('\n' + '-' * 22 + f'Task {t}' + '-' * 22)


# Task 1.
separator(1)
verse = task_1.open_verse()
print('Five most common letters:', *task_1.get_five(verse))

# Task 2.
separator(2)
cars = task_2.create_cars()
task_2.print_cars(cars)

# Task 3.
separator(3)
three_highest_cars = task_3.three_highest(cars)
three_fastest_cars = task_3.three_fastest(cars)
print('The highest cars:')
task_2.print_cars(three_highest_cars)
print('\nThe most powerful cars:')
task_2.print_cars(three_fastest_cars)

# Task 4.
separator(4)
cars = task_4.create_cars()
fastest_cars = task_3.three_fastest(cars)
print("===== Before Boost =====")
task_2.print_cars(fastest_cars)
task_4.boost_cars(fastest_cars)
print("===== After Boost =====")
task_2.print_cars(fastest_cars)

# Task 5.
separator(5)
cars = task_5.create_cars()
fastest_cars = task_3.three_fastest(cars)
for car in fastest_cars:
    print(f'{car.brand} {car.model} fuel consumption: {car.consumption}L or {car.miles_per_gallon()} mpg')

# Task 6.
separator(6)
combinations = task_6.all_combinations()
cubes_sums = task_6.all_sums(combinations)
most_common_sums = task_6.most_common_sums(cubes_sums)

print('Three most common sums:', *[s[0] for s in most_common_sums])

# Task 7.
separator(7)
iris = np.genfromtxt('iris.csv', delimiter=',')
iris = np.select([iris >= 3, iris < 3], [iris, -iris])
print(iris[:15])
