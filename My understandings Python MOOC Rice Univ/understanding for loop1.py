control=range(1,4,1)
e=[]
f=[]
def p():
    global e,f
    for redundent in control:
        e.append(control)
        f.append(redundent)
        print 'variable e'
        print e
        print 'variable f'
        print f
        
p()
''' 
in the for loop we have a redundent variable assumed to belong 
to the list declared in global variable
the redundent variable cannot be edited
the control variable controlls the execution of foe loop 
i.e how many times the for loop must execute
control variable cannot be editted
control and redundent can be used inside for loop as 
appending variables
'''