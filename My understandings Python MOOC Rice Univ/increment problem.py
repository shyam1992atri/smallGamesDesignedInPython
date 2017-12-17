import simplegui
number=0
def increment():
    return str(number)


def tick():
    global number
    number = number+1
    print number
    
def draw(canvas):
    canvas.draw_text(increment(),[50,50],25,'White')

    
frame=simplegui.create_frame('test',300,300)
timer=simplegui.create_timer(1000,tick)
frame.set_draw_handler(draw)
frame.start()
timer.start()

#why is nothing being printed on canves
 