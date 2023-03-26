import turtle

turtle.pensize(2)

for i in range(0,500,20):
    turtle.forward(i)
    turtle.left(90)

turtle.Screen().exitonclick()
