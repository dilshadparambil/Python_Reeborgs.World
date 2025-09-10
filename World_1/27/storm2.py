def collect_straight():
    while front_is_clear():
        while object_here():
            take()
        move()
        while object_here():
            take()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def straight():
    collect_straight()
    turn_right()
    move()
    turn_right()
    collect_straight()
    turn_left()
    
def first_move():
    move()
    turn_left()
    move()
    move()
    turn_left()
    move()
    turn_right()
    straight()

first_move()
for _ in range(2):
    move()
    turn_left()
    straight()
    
turn_left()
turn_left()
collect_straight()
turn_right()
while carries_object():
    toss()

    
    
    