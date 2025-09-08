def collect_straight():
    while front_is_clear():
        move()
        while object_here():
            take()

def turn_around():
    turn_left()
    turn_left()

for _ in range(2):
    collect_straight()
    turn_around()
    
turn_left()

while carries_object():
    toss()