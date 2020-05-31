import turtle as tl   # import turtle module of Python and rename it as tl

# ---- initialize turtle graphic window ------------
scn = tl.Screen()     # Creates a playground for turtles and assign it to variable scn
scn.bgcolor('lightblue') # set screen background color

# create and set pens
pen = tl.Turtle()     # Create a turtle, assign to variable named pen
pen.color('red')      # set pen color
pen.pensize(2)        # set pen size
pen.shape('arrow')   # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

pen.speed(2)          # set pen moving speed

# -----move the pen to draw ------------

# draw function y=x*x
scale = 10
pen.penup()
for x in range(-10, 11):
    y = x*x
    pen.goto(x*scale,y)
    pen.pendown()

# draw 2-D coordinate axes 
pen.color('blue')
pen.penup()
pen.goto(-20*scale, 0)
pen.pendown()
pen.goto(20*scale, 0)
pen.stamp()

pen.penup()
pen.goto(0, -20*scale)
pen.pendown()
pen.goto(0, 20*scale)
pen.left(90)
pen.stamp()



