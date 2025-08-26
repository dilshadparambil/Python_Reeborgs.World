def enter_plot():
    move()
    move()
    turn_left()
    move()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def harvest_row():
    for i in range(6):
        while object_here():
            take()
        move()
        
    else:
        if is_facing_north():
            turn_right()
            move()
            turn_right()
            move()
        else:
            turn_left()
            move()
            turn_left()
            move()

enter_plot()
for i in range(6):
    harvest_row()
