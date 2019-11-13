import turtle

turtle.colormode(255)#brings in the colormode functions
turtle.bgcolor('black')

bob = turtle.Turtle()
bob.pensize(10)#explore pensize
bob.speed(11)

for n in range(255):#use the loop variable for the color values
    c = (255,n,n)#explore use of r,g,b values
    bob.color(c)
    bob.circle(n)
    bob.right(200)
