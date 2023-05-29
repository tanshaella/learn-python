# Write a program that reads a sequence of grades (till 'done' is entered), and prints the average.

#         Example
# Enter grades in separate lines.
# To end the input type 'done':
# 71
# 86
# 68
# 94
# done
# The class average is 79.75

# variable: seen_done, grades_sum, students_count, current


print("Enter grades in separate lines. To end the input type 'done':")

grades_sum = 0
students_count = 0
seen_done = False
while(seen_done == False):
    curr_input = input()
    if(curr_input == 'done'):
        seen_done = True
    else:
        curr_grade = int(curr_input)
        grades_sum += curr_grade
        students_count += 1

average = grades_sum / students_count
print("The class average is", average)
