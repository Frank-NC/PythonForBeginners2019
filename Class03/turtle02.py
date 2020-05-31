import turtle as tl   # import turtle module of Python and rename it as tl

# ---- initialize turtle graphic window ------------
scn = tl.Screen()     # Creates a playground for turtles and assign it to variable scn
scn.bgcolor('lightblue') # set screen background color

# create and set pens
pen = tl.Turtle()     # Create a pen, assign to variable named pen
pen.color('red')      # set pen color
pen.pensize(2)        # set pen size
pen.shape('turtle')   # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

pen.speed(1)          # set pen moving speed

# -----move the pen to draw ------------
# draw a triangle
pen.forward(200)
pen.left(120)
pen.forward(200)
pen.left(120)
pen.forward(200)

# ------ create another pen -----
pen_2 = tl.Turtle()
pen_2.color('green')
# use default pen size and shape

# ----- draw a square -----------
pen_2.forward(200)
pen_2.left(90)
pen_2.forward(200)
pen_2.left(90)
pen_2.forward(200)
pen_2.left(90)
pen_2.forward(200)
pen_2.left(90)






