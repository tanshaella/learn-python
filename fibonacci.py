# Write a program to print first n Fibonacci Numbers

print("Please enter a positive integer greater than 1:")
input_num1=int(input())

for n in range(1,input_num1+1):
    n = 1
    for n2 in range(2,input_num1+1,2):
        n2 = 1
    print(n + n2)

