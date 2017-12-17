import simplegui
value=33

#draw handler
def draw(canvas):
    canvas.draw_text(str(value),[100,100],24,'White')

#define input field handler
def input_handler(text):
    global value
    value=float(text)


#create frame 
frame=simplegui.create_frame('test',200,200)

#regester handler
frame.set_draw_handler(draw)
frame.add_input('enter value',input_handler,100)
#start
frame.start()
