import turtle

sc = turtle.Screen()
sc.title("Chode Gobbler")
sc.bgcolor("orange")
sc.setup(width=1000, height=600)

# #left paddle
# left_pad = turtle.Turtle()
# left_pad.speed(0)
# left_pad.color("black")
# left_pad.shape("square")
# left_pad.shapesize(stretch_wid=6, stretch_len=2)
# left_pad.penup()
# left_pad.goto(-400, 0)

# # Right paddle
# right_pad = turtle.Turtle()
# right_pad.speed(0)
# right_pad.shape("square")
# right_pad.color("black")
# right_pad.shapesize(stretch_wid=6, stretch_len=2)
# right_pad.penup()
# right_pad.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.dx = -5
hit_ball.dy = -5
hit_ball.xcor = 0
hit_ball.ycor = 0
hit_ball.goto(hit_ball.xcor, hit_ball.ycor)

def move_ball():
    print("chode")

while True:
    sc.update()

    #update ball position
    hit_ball.goto(hit_ball.pos()[0] + hit_ball.dx, hit_ball.pos()[1] + hit_ball.dy)

    #check collision with wall
    if hit_ball.pos()[0] < -50:
        hit_ball.dy = hit_ball.dy*-1
        hit_ball.xcor = hit_ball.pos()[0] + 10
        
    if hit_ball.pos()[0] > 50:
        hit_ball.dy = hit_ball.dy*-1
        hit_ball.xcor = hit_ball.pos()[0] - 10
        
    if hit_ball.pos()[1] < -50:
        hit_ball.dy = hit_ball.dy*-1
        hit_ball.ycor = hit_ball.pos()[0] + 10
        
    if hit_ball.pos()[1] > 50:
        hit_ball.dy = hit_ball.dy*-1
        hit_ball.ycor = hit_ball.pos()[0] - 10