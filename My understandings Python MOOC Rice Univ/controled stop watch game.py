# "Stopwatch: The Game"
import simplegui
# define global variables
time='0:00.0'
win_count=0
stop_count=0
interval=100
second=0
minute=0
milli_second=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time(t):
    global interval,second,minute
    milli_second=((interval/1000)*10)%10
    if milli_second==0:
        second=interval/1000
        if second==60:
            second=0
            interval=100
            minute=minute+1

    #print str(minute)+' : '+ str(second) +' . '+str(((interval/1000)*10)%10)+'\n'    
    return str(minute)+str(':')+str(int(second/10))+str(second%10)+str('.')+str(milli_second)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    global interval,minute,win_count,stop_count
    interval=0
    win_count=0
    stop_count=0
    minute=0
    timer.stop()

   
def start():
    timer.start()
    return format_time('100')
    
def stop():
    timer.stop()
    global win_count,interval,stop_count,second,minute,counter
    zero_count=((interval/1000)*10)%10
    if zero_count==0:
        win_count=win_count+1
    stop_count=stop_count+1
    if stop_count==10:
        reset()
        

    
        

# define event handler for timer with 0.1 sec interval
def tick():
    global interval
    interval=interval+100
    
    

# define draw handler
def draw(canvas):
    canvas.draw_text('INSTRUCTIONS',[1,355],25,'Yellow')
    canvas.draw_text('How to play',[1,375],25,'Yellow')
    canvas.draw_text('1.Initially press reset to initialise the game.',[1,400],25,'White')
    canvas.draw_text('2.press start to start the game.',[1,430],25,'White')
    canvas.draw_text('3.press stop to increase your win count.',[1,460],25,'White')
    canvas.draw_text('4.press start to continue with the game.',[1,490],25,'White')
    canvas.draw_text('5.your win count increases if the millisecond part is zero.',[1,520],25,'White')
    canvas.draw_text('6.press reset to reset the game.',[1,550],25,'White')
    canvas.draw_text(format_time('100'),[230,225],50,'White')
    canvas.draw_text('win count '+str(win_count) +' / ' +'stop count '+str(stop_count),[125,50],25,'Orange')
    canvas.draw_circle((300,230),125,5,'Blue')
    canvas.draw_circle((200,130),8,15,'Violet')
    canvas.draw_circle((300,100),8,15,'Green')
    canvas.draw_circle((400,130),8,15,'Red')
    canvas.draw_text('7.if stop count=10 the game automatically resets',[1,575],25,'Yellow')
    
# create frame
frame=simplegui.create_frame('Stop watch game',600,600)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('reset',reset)
frame.add_button('start',start)
frame.add_button('stop',stop)
timer=simplegui.create_timer(interval,tick)

# start frame
frame.start()


# Please remember to review the grading rubric
