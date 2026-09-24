import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Animation")
screen.setup(800,700)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

def heart(t, scale):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4 * t)
    return x * scale , y * scale

offset = 0
def animate():
    global offset
    pen.clear()
    for i in range(180):
        t = (i / 180) * 2 * math.pi
        x , y = heart(t, 15)

        x += math.sin(offset + i * 0.15)
        y += math.cos(offset + i * 0.12)

        pen.goto(x, y)
        pen.dot(5, "red")

    offset += 0.15
    screen.ontimer(animate, 30)

animate()
screen.mainloop()


