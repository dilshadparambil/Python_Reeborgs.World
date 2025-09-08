def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def build():
    turn_right()
    build_wall()
    turn_left()
 
move()
turn_right()
move()
while not at_goal():
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        build()
    else:
        move()


    
    
