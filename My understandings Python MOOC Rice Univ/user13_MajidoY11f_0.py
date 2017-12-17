
import simplegui

# Initialize globals
width = 200
hight=200
number = 5



# define event handlers


def draw(canvas):
    global number
    canvas.draw_text(str(number),[100,100],25,'white')
    

def keydown(key):
    global number
    if key==simplegui.KEY_MAP['up']:
        number=number+number
        
def keyup(key):
    global number
    if key==simplegui.KEY_MAP['up']:
        number=number-3
    
                               
# create frame
frame = simplegui.create_frame("Motion", width, hight)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
frame.start()

