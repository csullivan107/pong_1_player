import pgzrun
import random

#things to do next time
#   -make sure dx is always positive
#   -look into ball.dy bug... sometimes it seems to plane out then go opposite

WIDTH = 1000
HEIGHT = 800

ball = Actor('ball')
ball.center = WIDTH/2, HEIGHT/2
ball.dx = random.randrange(0,10)
ball.dy = random.randrange(0,10)

paddle = Actor('paddle')
paddle.center = 50,HEIGHT/2 
paddle.dy = 5
paddle.score = 0

def game_reset():
    ball.center = WIDTH/2, HEIGHT/2
    paddle.score = 0
    ball.dx = random.randrange(0,10)
    ball.dy = random.randrange(0,10)
    paddle.center = 50,HEIGHT/2 

def draw():
    screen.clear()
    ball.draw()
    paddle.draw()
    screen.draw.text(str(paddle.score), centerx=WIDTH/2, centery = 20, fontsize = 50 )

def update():
    #update ball position
    ball.center = ball.center[0] + ball.dx, ball.center[1] + ball.dy

    #check for screen collisions

    #bounce off the right side
    if (ball.right > WIDTH): 
        ball.dx = ball.dx*-1 #flip direction
        #ensure ball position valid for continuing
        ball.right = WIDTH - ball.dx

    #bounce off paddle condition
    if (ball.left <= paddle.right) and (paddle.bottom >= ball.center[1]) and (paddle.top <= ball.center[1]):
        ball.dx = ball.dx*-1
        ball.left = paddle.right + ball.dx
        paddle.score += 1
        #up the difficulty
        ball.dx += 1
        ball.dy += 1

    #Loss condition
    if (ball.right < 0): 
        game_reset()

    #bounce off ceiling
    if (ball.bottom > HEIGHT): 
        ball.dy = ball.dy*-1 #flip direction
        #ensure ball position valid for continuing
        ball.bottom = HEIGHT - ball.dy

    #bounce off floor
    if (ball.top < 0): 
        ball.dy = ball.dy*-1 #flip direction
        #ensure ball position valid for continuing
        ball.top = 0 + ball.dy

    #move paddle
    if keyboard.up:
        paddle.centery += -1*paddle.dy

    if keyboard.down:
        #check if on screen???
        paddle.centery = paddle.centery + paddle.dy

    


pgzrun.go()
