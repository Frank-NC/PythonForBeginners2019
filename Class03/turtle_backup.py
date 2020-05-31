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

pen.forward(150)        # pen move forward by 150 pixels
pen.penup()             # lift pen up
pen.forward(50)         # pen move forward by 50 pixels
pen.left(90)            # turn pen by 90 degrees to the left
pen.pendown()           # put pen down
pen.forward(150)        # pen move forward by 150 pixels
pen.penup()             # lift pen up
pen.forward(50)         # pen move forward by 50 pixels




