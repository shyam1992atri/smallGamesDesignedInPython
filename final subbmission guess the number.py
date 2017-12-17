print '''to run 1000 number game doc string out 100 number game
and un comment out the 1000 number game code written at
the bottom\n '''
print '''computer chooses a number between 1 to 100 and 
the player has to enter his guess in the box that pops up\n''' 

import simplegui
import random
counter=7
user_guess=0
computer_choice100=random.randrange(1,100,1)


          
def enter(inp):
    global user_guess
    user_guess=int(inp)
    range100()
  


def initialise():
    global computer_choice100
    computer_choice100=random.randrange(1,100,1)


def count():
    global counter
    print 'chance number',counter
    counter=counter-1
    print 'remaining chances',counter,'\n'
    
    
    
    
def range100():
    global user_guess
    global counter
    global computer_choice100
   
   
    
    if computer_choice100>user_guess and counter>0:
        print 'computer choice is higher than',user_guess,' and user guess is',user_guess
        count()
    elif computer_choice100<user_guess and counter>0 :
        print 'computer choice is  lower than',user_guess,' and user guess is',user_guess
        count()
    elif computer_choice100==user_guess :
        print 'correct guess'
        print 'computer choice was',computer_choice100
        print 'end of game'
        print 'begining new game\n'
        counter=8
        print 'counter 8 is a dummy counter that starts in the next game'
        start_new100()
    elif counter<0:
        print 'u r out of chances',counter
        print 'computer choice was',computer_choice100,'\n'
        print 'begining new game\n'
        counter=8
        print 'counter 8 is a dummy counter that starts in the next game'
        start_new100() 
    else :
        print 'end of game'
        print 'computer choice was',computer_choice100,'\n'
        count()
        start_new100()
          
    
def start_new100():
    
    print 'enter u r input'
    global counter 
    counter=8
    print 'counter 8 is a dummy counter that starts in the next game'
    print 'remaining chances',counter,'\n'
    initialise()
    range100()
    
    
    


    
f=simplegui.create_frame('guess the number game',300,300)
f.add_button('new range100',start_new100,100)

f.add_input('user guess',enter,100)
f.start()

'''
import simplegui
import random
counter=10
user_guess=0
computer_choice1000=random.randrange(1,1000,1)


          
def enter(inp):
    global user_guess
    user_guess=int(inp)
    range1000()
  


def initialise():
    global computer_choice1000
    computer_choice1000=random.randrange(1,1000,1)


def count():
    global counter
    print 'chance number',counter
    counter=counter-1
    print 'remaining chances',counter,'\n'
    
    
    
    
def range1000():
    global user_guess
    global counter
    global computer_choice1000
   
   
    
    if computer_choice1000>user_guess and counter>0:
        print 'computer choice is higher than',user_guess,' and user guess is',user_guess
        count()
    elif computer_choice1000<user_guess and counter>0 :
        print 'computer choice is  lower than',user_guess,' and user guess is',user_guess
        count()
    elif computer_choice1000==user_guess :
        print 'correct guess'
        print 'computer choice was',computer_choice1000
        print 'end of game'
        print 'begining new game\n'
        counter=11
        print 'counter 11 is a dummy counter that starts in the next game'
        start_new1000()
    elif counter<0:
        print 'u r out of chances',counter
        print 'computer choice was',computer_choice1000,'\n'
        print 'begining new game\n'
        counter=11
        print 'counter 11 is a dummy counter that starts in the next game'
        start_new1000() 
    else :
        print 'end of game'
        print 'computer choice was',computer_choice1000,'\n'
        count()
        start_new1000()
          
    
def start_new1000():
    
    print 'enter u r input'
    global counter 
    counter=11
    print 'counter 11 is a dummy counter that starts in the next game'
    print 'remaining chances',counter,'\n'
    initialise()
    range1000()
    
    
    


    
f=simplegui.create_frame('guess the number game',300,300)
f.add_button('new range1000',start_new1000,100)

f.add_input('user guess',enter,1000)
f.start()
'''