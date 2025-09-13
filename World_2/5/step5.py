def pick_two_berries():
    move()
    take()
    move()
    take()
    turn_left()
    turn_left()
    move()
    move()
    put()
    put()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

for i in range(2):
    move()
    turn_left()
    pick_two_berries()
    turn_left()
    move()
    turn_right()
    pick_two_berries()
    turn_right()
    
move()
move()
