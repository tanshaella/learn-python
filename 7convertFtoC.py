# Write a program that reads from the user a temperature in Fahrenheit degrees and converts it to its Celsius equivalent.

def main():
    print("Please enter a temperature in Fahrenheit:")
    fahr=float(input())
    cel = fahrenheit_to_celsius(fahr)
    print(fahr, "Fahrenheit is", cel, "Celsius")

def fahrenheit_to_celsius(F):
    C=(F-32)*(5/9)
    return C

main()
