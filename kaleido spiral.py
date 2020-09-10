import turtle as t
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple','pink'])
global count
def draw_circle(size,angle,shift):
    
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    '''while count<10:
        draw_circle(size+5)'''
        

def intro():
    try:
        color = input('\'Welcome to Kaleido-spiral\'\nEnter the background colour: ')
    except:
        color = 'black'

    speed = input('Enter the art speed:\nFor slowest enter 1\nSlow 2\nNormal 3\nFast 4\nFastest 5: ')
    try:
        rep = int(input('Enter the number of repetitions: '))
    except:
        print('Invalid repetition number, Input an integer')
        intro()
        
    if speed == '1':
        speed = 'slowest'
    elif speed == '2':
        speed = 'slow'
    elif speed == '3':
        speed = 'normal'
    elif speed == '4':
        speed = 'fast'
    elif speed == '5':
        speed = 'fastest'
    else :
        print ('Wrong input')
        intro()
    try:
        t.bgcolor(color)
    except:
        t.bgcolor('black')
    t.speed(speed)
    t.pensize(4)
    count=0
    x,y,z=30,0,1
    while count<rep:
        draw_circle(x,y,z)
        x+=5
        y+=1
        z+=1
        count+=1


intro()
