import turtle
pen = turtle.Turtle()
turtle.bgcolor('black')
pen.speed(1)
pen.colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for i in range(300):
    pen.pencolor(pen.colors[i % 6])
    pen.forward(i * 2)
    pen.right(61)
turtle.done()