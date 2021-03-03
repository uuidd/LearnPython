import turtle



def turtle_test():
    tt = turtle.Pen()
    tt.showturtle()
    tt.write("高淇")
    tt.forward(300)
    tt.color("red")
    tt.left(90)
    tt.forward(300)
    tt.goto(0,50)
    tt.goto(0,0)
    tt.penup()
    tt.goto(0,300)
    tt.goto(0,0)
    tt.pendown()
    tt.goto(0,50)
    tt.goto(50,50)
    tt.circle(100)


def draw_circle():
    tt = turtle.Pen()
    colors = ("red", "green", "yellow", "black", "blue")
    tt.width(4)
    tt.speed(0)
    for i in(range(100)):
        tt.penup()
        tt.goto(0, -i * 20)
        tt.pendown()
        tt.color(colors[i%len(colors)])
        tt.circle(25 + i * 20)

def draw_line(size, width):
    tt = turtle.Pen()
    tt.speed(20)
    for i in range(size*2//width +1):
        tt.penup()
        tt.goto(-size, size - i * width)
        tt.pendown()
        tt.forward(size * 2)
    tt.right(90)
    for i in range(size*2//width +1):
        tt.penup()
        tt.goto(-size + i * width, size)
        tt.pendown()
        tt.forward(size * 2)

draw_line(200,20)


