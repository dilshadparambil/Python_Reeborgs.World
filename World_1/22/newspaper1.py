def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def up():
    turn_left()
    move()
    turn_right()
    move()
    move()

def down():
    move()
    move()
    turn_left()
    move()
    turn_right()
    
take()
for _ in range(3):
    up()

while object_here():
    take()
put('star')
turn_left()
turn_left()
for _ in range(3):
    down()

        
