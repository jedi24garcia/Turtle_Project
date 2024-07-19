import turtle
pen = turtle.Turtle()
pen.fillcolor("red")
turtle.bgcolor('black')
pen.speed(0)
pen.colors = ["red"]
for i in range(300):
    pen.pencolor(pen.colors[i % 1])
    pen.forward(i * 2)
    pen.right(61)


turtle.done()