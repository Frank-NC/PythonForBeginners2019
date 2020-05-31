import turtle as tl   # import turtle module of Python and rename it as tl

# ---- initialize turtle graphic window ------------
scn = tl.Screen()     # Creates a playground for turtles and assign it to variable scn
scn.bgcolor('lightblue') # set screen background color

# create and set pens
pen = tl.Turtle()     # Create a turtle, assign to variable named pen
pen.color('red')      # set pen color
pen.pensize(2)        # set pen size
pen.shape('turtle')   # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

pen.speed(1)          # set pen moving speed

# -----move the pen to draw ------------

pen.forward(150)
pen.setheading(390)
print(390, pen.heading())

pen.setheading(181)
print(181, pen.heading())

pen.setheading(-45)
print(-45, pen.heading())

pen.setheading(-181)
print(-181, pen.heading())

pen.setheading(135)
print(135, pen.heading())

pen.setheading(270)
print(270, pen.heading())




