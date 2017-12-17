# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# import random first
import random

def number_to_name():
    # this code is for the computer to choose
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    number=random.randint(0,4)
    if number==0:
        print 'computer chooses rock'
        return 0
    elif number==1:
        print 'computer chooses spock'
        return 1
    elif number==2:
        print 'computer chooses paper'
        return 2
    elif number==3:
        print 'computer chooses lizard'
        return 3
    elif number==4:
        print 'computer chooses scissor'
        return 4
    else :
        print 'wrong choise'
        
    
    


    
def name_to_number(name):
    
    #this function is for the player to choose his choice

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name=='rock':
        print 'player chooses rock'
        return 0
    elif name=='spock':
        print 'player chooses spock'
        return 1
    elif name=='paper':
        print 'player chooses paper'
        return 2
    elif name=='lizard':
        print 'player chooses lizard'
        return 3
    elif name=='scissors':
        print 'player chooses scissors'
        return 4
    else:
        print 'wrong choice'
        
    
       
    
    


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results
    name_new=name_to_number(name)
    number_new=number_to_name()
    mod_difference=(name_new-number_new)%5
    if mod_difference==1 or mod_difference==2:
        print 'player winns !\n'
    elif mod_difference==3 or mod_difference==4:
        print 'computer winns !\n'
    else :
        print 'the game has ended in a tie\n'
        


    
# test your code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
# 
#http://www.codeskulptor.org/#user10_iyEMBfR4Po00Mqk_0.py