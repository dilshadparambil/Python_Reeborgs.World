count=0
def find_center(count):
    while front_is_clear():
        count+=1
        move()
        if wall_in_front():
            turn_left()
            turn_left()
            break
    
    for i in range(int(count/2)):
        move()

find_center(count)
while not is_facing_north():
    turn_left()
find_center(count)
    
put()
