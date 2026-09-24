import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Animation")
screen.setup(800, 700)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

def get_heart_pos(t, scale):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x * scale, y * scale

total_points = 100
scale = 15
text = "I love you"
font = ("Arial", 9, "bold")

progress = 0
blink_state = True
filled = False

def animate():
    global progress, blink_state, filled
    
    pen.clear()
    
    current_max = int(progress)
    
    for i in range(total_points):
        if i > current_max:
            break
            
        t = (i / total_points) * 2 * math.pi
        adjusted_t = t + (3 * math.pi / 2) 
        
        x, y = get_heart_pos(adjusted_t, scale)
        
        should_draw = True
        if not blink_state:
            should_draw = False
        
        if should_draw:
            pen.goto(x, y)
            pen.color("#ff6b9d")
            pen.write(text, align="center", font=font)

    if not filled:
        if progress < total_points:
            progress += 0.8
        else:
            filled = True
            blink_state = not blink_state
    else:
        blink_state = not blink_state
        
    screen.update()
    screen.ontimer(animate, 50)

animate()
screen.mainloop()