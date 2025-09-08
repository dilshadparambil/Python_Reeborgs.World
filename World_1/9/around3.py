def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()
if wall_in_front():
    turn_left()
move()

while not object_here():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
