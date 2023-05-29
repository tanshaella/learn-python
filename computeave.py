# Write a program that reads grades of students in a class, and prints the average.

# number_of_students, curr_grade, grades_sum, average


print("Please enter the number of students in the class:")
number_of_students = int(input())

print("Please enter students' grades (in separate lines):")
grades_sum = 0
for i in range(number_of_students):
    curr_grade = int(input())
    grades_sum += curr_grade

average = grades_sum / number_of_students
print("The class average is", average)
