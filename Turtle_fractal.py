import turtle

turtle.bgcolor("black")
arv = turtle.Turtle()
arv.pensize(2)
arv.pencolor("green")
arv.left(90)
arv.backward(100)
arv.speed(2000)

def drawTree(i):
    if i< 10:
        print("Inside")
        return
    else:
        print("Outside")
        arv.forward(i)
        arv.color("magenta")
        arv.circle(2)
        arv.color("brown")
        arv.left(30)
        drawTree(3*i/4)
        arv.right(60)
        drawTree(3*i/4)
        arv.left(30)
        arv.backward(i)

drawTree(100)
turtle.done()