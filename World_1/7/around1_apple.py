def move_straight():
    for i in range(9):
        if object_here():
            take()
        move()
        
for i in range(4):
    move_straight()   
    turn_left()
    
