import turtle        #1st step
def turtle_square(side_len):        #2
    for i in range(4):        #7 10 13 16 19 22
        turtle.forward(side_len)
        turtle.left(90)
print("Please enter number of squares:")        #3
n=int(input())        #4
# draw a fan of n squares (100x100)
for count in range(n):        #5
    turtle_square(100)        #6 9 12 15 18 21
    turtle.left(360/n)        #8 11 14 17 20 23
turtle.hideturtle()
turtle.done()

