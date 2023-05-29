import turtle
def turtle_square(side_len):
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)
def main():
    print("Please enter number of squares:")
    n=int(input())
    turtle_fan_of_squares(n,100)
    turtle.hideturtle()
    turtle.done()
def turtle_fan_of_squares(num_of_sqrs,side_len):
    for count in range(num_of_sqrs):
        turtle_square(side_len)
        turtle.left(360/num_of_sqrs)

main()

# (1) main, (2) other functions

