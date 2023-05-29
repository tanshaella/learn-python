# Write a program that reads a positive integer n, and prints a n*n multiplication table.

# Write a program that reads a positive integer n, and prints the first n multiplications of 3.

print("Please enter a positive integer:")
n = int(input())

for row in range(1,n+1):
    for i in range(1,n+1):
        print(row*i, end='\t')
    print('')
