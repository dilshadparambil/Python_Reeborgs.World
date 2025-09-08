def turn_right():
    turn_left()
    turn_left()
    turn_left()

put()
move()
while not object_here():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
