# Ball motion with an explicit timer

import simplegui

# Initialize globals
width = 600
hight = 400
ball_radius = 20
ball_pos=[width/2,hight/2]
vel=[0,0]

# define event handlers


def draw(canvas):
    ball_pos[0]=ball_pos[0]+vel[0]
    ball_pos[1]=ball_pos[1]+vel[1]
    if ball_pos[0]<=0+ball_radius:
        vel[0]=-vel[0]
    elif ball_pos[0]>=width-1-ball_radius:
        vel[0]=-vel[0]
    elif ball_pos[1]<=0+ball_radius:
        vel[1]=-vel[1]
    elif ball_pos[1]>=hight-1-ball_radius:
        vel[1]=-vel[1]
    
    canvas.draw_circle(ball_pos,ball_radius, 2, "Red", "White")

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

