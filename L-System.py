import turtle

#Config. Screen
WIDTH, HEIGHT = 1000,800
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.screensize(3*WIDTH,3*HEIGHT)
screen.bgcolor('black')
screen.delay(0)

#Config. Turtle
trig = turtle.Turtle()
trig.pensize(2)
trig.speed(0)
trig.setpos(-WIDTH //3, -HEIGHT//2)
trig.color('green')

#L-System
generation = 14
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', 'GG'
step = 8
angle = 120

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else
                    rule_2 if chr == chr_2 else chr for chr in axiom])

def get_result(generation, axiom):
    for gen in range(generation):
        axiom = apply_rules(axiom)
    return axiom

axiom = get_result(generation, axiom)

for chr in axiom:
    if chr == chr_1 or chr ==chr_2:
        trig.forward(step)
    elif chr == '+':
        trig.right(angle)
    elif chr == '-':
        trig.left(angle)

screen.exitonclick()
