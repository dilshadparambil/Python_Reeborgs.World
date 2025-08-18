put()
if front_is_clear():
    move()
else:
    turn_left()
    move()
    
while not object_here():
    if wall_in_front():
        turn_left()
        move()
    else :
        move()
