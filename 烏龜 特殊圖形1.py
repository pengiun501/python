import turtle
t=turtle.Turtle()
t.screen.reset()
t.color('blue')
t.shape('circle')
t.pensize('5')

i=1
while True:
    t.forward(i)
    t.left(30)
    i=i+1