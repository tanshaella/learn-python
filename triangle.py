# Write a program that reads a positive integer n and prints a n line right triangle, aligned to the let with '*' symbols.

print("Please enter a positive integer")
n = int(input())

for n in range(1,n+1):
    print(n*"*")
