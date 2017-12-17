# Ball motion with an explicit timer

import simplegui
import random

# Initialize globals
width = 600
hight = 400
total_hight=620
bar_hight_left=80
bar_width_left=8
bar_left=[bar_width_left/2,bar_hight_left/2]
bar_hight_right=80
bar_width_right=8
bar_right=[bar_width_right/2+590,bar_hight_right/2]
vel_left=[0,0]
vel_right=[0,0]
ball_radius = 20
ball_pos=[width/2,hight/2]
pad_width_1eft=10
pad_width_right=590
vel=[0,0]
left_point=0
right_point=0

# define event handlers
def reset():
    global vel_left,vel_right,vel,ball_pos
    vel_left=[0,0]
    vel_right=[0,0]
    vel=[0,0]
    ball_pos=[width/2,hight/2]
    bar_left=[bar_width_left/2,bar_hight_left/2]
    bar_right=[bar_width_right/2+590,bar_hight_right/2]
    left_point=0
    right_point=0

    


def draw(canvas):
    global left_point,right_point
    canvas.draw_polygon([(bar_left[0]-bar_width_left/2,bar_left[1]+bar_hight_left/2),(bar_left[0]+bar_width_left/2,bar_left[1]+bar_hight_left/2),(bar_left[0]+bar_width_left/2,bar_left[1]+bar_hight_left/2),(bar_left[0]+bar_width_left/2,bar_left[1]-bar_hight_left/2),(bar_left[0]-bar_width_left/2,bar_left[1]-bar_hight_left/2)],10,'Red')
    canvas.draw_polygon([(bar_right[0]-bar_width_right/2,bar_right[1]+bar_hight_right/2),(bar_right[0]+bar_width_right/2,bar_right[1]+bar_hight_right/2),(bar_right[0]+bar_width_right/2,bar_right[1]+bar_hight_right/2),(bar_right[0]+bar_width_right/2,bar_right[1]-bar_hight_right/2),(bar_right[0]-bar_width_right/2,bar_right[1]-bar_hight_right/2)],10,'Blue')
    bar_left[1]=bar_left[1]+vel_left[1]
    bar_right[1]=bar_right[1]+vel_right[1]
    if bar_left[1]<0+40:
        vel_left[1]=-vel_left[1]
    elif bar_left[1]>hight-1-40:
        vel_left[1]=-vel_left[1]
    elif bar_right[1]<0+40:
        vel_right[1]=-vel_right[1]
    elif bar_right[1]>hight-1-40:
        vel_right[1]=-vel_right[1]
    
    ball_pos[0]=ball_pos[0]+vel[0]
    ball_pos[1]=ball_pos[1]+vel[1]
    if ball_pos[0]<=0+30:
        if ball_pos[1]>=bar_left[1]-40 and ball_pos[1]<=bar_left[1]+40 :
            vel[0]=-vel[0]
            vel[1]=-vel[1]
            vel_left[0]=0
            vel_left[1]=0
            left_point=left_point+2
            
        else :
            ball_pos[0]=width/2
            ball_pos[1]=hight/2
            vel[0]=-vel[0]+0.1
            vel[1]=random.randrange(1,5,1)
            left_point=left_point-1
    elif ball_pos[0]>=width-1-30:
        if ball_pos[1]>=bar_right[1]-40 and ball_pos[1]<=bar_right[1]+40 :
            vel[0]=-vel[0]
            vel[1]=-vel[1]
            vel_right[0]=0
            vel_right[1]=0
            right_point=right_point+2
        else :
            ball_pos[0]=width/2
            ball_pos[1]=hight/2
            vel[0]=-vel[0]-0.1
            vel[1]=random.randrange(-3,3,1)
            right_point=right_point-1
    elif ball_pos[1]<=0+ball_radius:
        vel[1]=-vel[1]
    elif ball_pos[1]>=hight-1-ball_radius:
        vel[1]=-vel[1]
    canvas.draw_circle(ball_pos,ball_radius, 2, "Red", "green")
    canvas.draw_line([width/2,0],[width/2,hight],1,'Black')
    canvas.draw_line([pad_width_1eft,0],[pad_width_1eft,hight],1,'Black')
    canvas.draw_line([pad_width_right,0],[pad_width_right,hight],1,'Black')
    canvas.draw_line([0,hight],[width,hight],1,'Black')
    canvas.draw_text('Red player point '+str(left_point),[30,450],25,'red')
    canvas.draw_text('Blue player point '+str(right_point),[350,450],25,'blue')
    canvas.draw_text('How To play',[10,500],25,'green')
    canvas.draw_text('1.Press space bar to start the game',[10,525],25,'green')

    
def keydown(key):
    acc=1
    if key==simplegui.KEY_MAP['down']:
        vel_right[1]=vel_right[1]+acc
    elif key==simplegui.KEY_MAP['up']:
        vel_right[1]=vel_right[1]-acc
    elif key==simplegui.KEY_MAP['s']:
        vel_left[1]=vel_left[1]+acc
    elif key==simplegui.KEY_MAP['w']:
        vel_left[1]=vel_left[1]-acc
    elif key==simplegui.KEY_MAP['space']:
        vel[0]=random.randrange(-1,2,2)
        vel[1]=random.randrange(-1,2,2)
        

    
                               
# create frame
frame = simplegui.create_frame("Motion", width, total_hight)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_canvas_background('yellow')
frame.add_button('Reset',reset)

# start frame
frame.start()