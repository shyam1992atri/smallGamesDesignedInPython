# Ball motion with an explicit timer

import simplegui

# Initialize globals
width = 600
hight = 400
bar_hight_left=80
bar_width_left=8
bar_left=[bar_width_left/2,bar_hight_left/2]
bar_hight_right=80
bar_width_right=8
bar_right=[bar_width_right/2+590,bar_hight_right/2]


# define event handlers


def draw(canvas):
    canvas.draw_polygon([(bar_left[0]-bar_width_left/2,bar_left[1]+bar_hight_left/2),(bar_left[0]+bar_width_left/2,bar_left[1]+bar_hight_left/2),(bar_left[0]+bar_width_left/2,bar_left[1]+bar_hight_left/2),(bar_left[0]+bar_width_left/2,bar_left[1]-bar_hight_left/2),(bar_left[0]-bar_width_left/2,bar_left[1]-bar_hight_left/2)],10,'white')
    canvas.draw_polygon([(bar_right[0]-bar_width_right/2,bar_right[1]+bar_hight_right/2),(bar_right[0]+bar_width_right/2,bar_right[1]+bar_hight_right/2),(bar_right[0]+bar_width_right/2,bar_right[1]+bar_hight_right/2),(bar_right[0]+bar_width_right/2,bar_right[1]-bar_hight_right/2),(bar_right[0]-bar_width_right/2,bar_right[1]-bar_hight_right/2)],10,'white')

def keydown(key):
    vel=4
    if key==simplegui.KEY_MAP['down']:
        bar_right[1]=bar_right[1]+vel
    elif key==simplegui.KEY_MAP['up']:
        bar_right[1]=bar_right[1]-vel
    elif key==simplegui.KEY_MAP['s']:
        bar_left[1]=bar_left[1]+vel
    elif key==simplegui.KEY_MAP['w']:
        bar_left[1]=bar_left[1]-vel    
    
                               
# create frame
frame = simplegui.create_frame("Motion", width, hight)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)


# start frame
frame.start()

