import turtle
t=turtle.Turtle()
t.screen.reset()
t.color('blue')
t.shape('circle')
t.pensize('5')
i=0
while i<4:
    i=i+1
    t.forward(100)
    t.left(90)    
t2=turtle.Turtle()
t2.color('white')
t2.pensize('1')
t2.shape('circle')
t2.backward(200)
t2.pensize('5')
t2.color('red')
i=0
while i<4:
    i=i+1
    t2.forward(100)
    t2.left(90)