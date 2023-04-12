import turtle

# Create a turtle object
t = turtle.Turtle()

# Define functions for drawing rectangle, circle, and eraser
def draw_rect():
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)

def draw_circle():
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.circle(50)

def draw_eraser():
    t.pencolor("white")
    t.pensize(20)
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    t.setheading(0)
    t.forward(200)
    t.penup()
    t.goto(-100, -80)
    t.pendown()
    t.setheading(0)
    t.forward(200)

# Define a function for color selection
def choose_color():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(len(colors)):
        t.penup()
        t.goto(-150 + i * 50, -150)
        t.pendown()
        t.pencolor(colors[i])
        t.dot(30)

# Main program
choose_color()  # Draw color selection
t.pencolor("black")  # Set initial pen color
t.pensize(5)  # Set initial pen size

# Listen for mouse clicks and execute appropriate functions
turtle.onscreenclick(draw_rect, btn=1)
turtle.onscreenclick(draw_circle, btn=2)
turtle.onscreenclick(draw_eraser, btn=3)
turtle.onscreenclick(choose_color)

# Start the turtle graphics window
turtle.mainloop()