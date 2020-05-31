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
pen.penup()                # This is new
step_size = 20
for i in range(30):
   pen.stamp()                 # stamp the canvas with current pen shape
   step_size = step_size + 3   # Increase the step size on every iteration
   pen.forward(step_size)      
   pen.right(24)         

   




