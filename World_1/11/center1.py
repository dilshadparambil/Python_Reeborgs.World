count=0
while front_is_clear():
    count+=1
    move()
    if wall_in_front():
        turn_left()
        turn_left()
        break
       
for i in range(int(count/2)):
    move()
    
put()
