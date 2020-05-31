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

# draw polygon of any number of edges
num = int(input("Please input number of edges: "))
angle = 180 - (num-2)*180/num

for i in range(num):
    pen.forward(40)
    pen.left(angle)






