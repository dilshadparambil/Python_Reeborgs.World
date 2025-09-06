def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_back_tile():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    
def build():
    turn_right()
    build_wall()
    turn_left()
 
while not at_goal():
    move()
    
turn_right()
move()

while not at_goal():
    if wall_in_front():
        turn_left()
    elif not wall_on_right():
        move()
        if wall_on_right():
            turn_back_tile()
            build()
        else:
            turn_back_tile()
            turn_right()
            move()
    else:
        move()


    
    
