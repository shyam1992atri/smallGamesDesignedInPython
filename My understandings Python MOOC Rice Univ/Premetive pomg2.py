# Ball motion with an explicit timer

import simplegui
import random

# Initialize globals
width = 600
hight = 400
ball_radius = 20
ball_pos=[width/2,hight/2]
pad_width_1eft=10
pad_width_right=590
vel=[0,0]
left_score=0
right_score=0

# define event handlers


def draw(canvas):
    ball_pos[0]=ball_pos[0]+vel[0]
    ball_pos[1]=ball_pos[1]+vel[1]
    global left_score,right_score
    canvas.draw_text(str(left_score),[400,100],30,'white')
    canvas.draw_text(str(left_score),[100,100],30,'white')
    
    if ball_pos[0]<=0+30:
        ball_pos[0]=width/2
        ball_pos[1]=hight/2
        vel[0]=-vel[0]+0.25
        left_score=left_score+2
        right_score=right_score-1
        vel[1]=random.randrange(1,5,1)
    elif ball_pos[0]>=width-1-30:
        ball_pos[0]=width/2
        ball_pos[1]=hight/2
        vel[0]=-vel[0]-0.25
        right_score=right_score+2
        left_score=left_score-1
        vel[1]=random.randrange(-3,3,1)
    elif ball_pos[1]<=0+ball_radius:
        vel[1]=-vel[1]
    elif ball_pos[1]>=hight-1-ball_radius:
        vel[1]=-vel[1]
    
    canvas.draw_circle(ball_pos,ball_radius, 2, "Red", "White")
    canvas.draw_line([width/2,0],[width/2,hight],1,'white')
    canvas.draw_line([pad_width_1eft,0],[pad_width_1eft,hight],1,'white')
    canvas.draw_line([pad_width_right,0],[pad_width_right,hight],1,'white')

def keydown(key):
    acc=1
    if key==simplegui.KEY_MAP['left']:
        vel[0]=vel[0]-acc
    elif key==simplegui.KEY_MAP['right']:
        vel[0]=vel[0]+acc
    elif key==simplegui.KEY_MAP['down']:
        vel[1]=vel[1]+acc
    elif key==simplegui.KEY_MAP['up']:
        vel[1]=vel[1]-acc
    
                               
# create frame
frame = simplegui.create_frame("Motion", width, hight)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)


# start frame
frame.start()

