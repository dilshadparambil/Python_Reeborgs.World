#home4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def L_shape(): 
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()

def next_L():
    turn_right()
    move()
    turn_right()
    
for i in range(3):
    L_shape()
    next_L()

L_shape()
