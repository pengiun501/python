import turtle
t=turtle.Turtle()
t.screen.reset()
t.color('blue')
t.shape('turtle')
t.pensize('5') 
for i in range(20):
    t.forward(i*10)
    t.left(30)