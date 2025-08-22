# Game 5: Around 1
  
## Around the World
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201&url=worlds%2Ftutorial_en%2Faround1.json)  
[Solution link](around1.py) 

Have Reeborg go around the world in the counter-clockwise direction once, and stop at its starting position. Reeborg must not step on the grass. The correct path is shown by the dashed white line.

## What you need to know:  
  - The functions `move()`, `turn_left()`, and `put()`.

### More Advanced:  
  - You can write a more general program, having Reeborg decide by itself when it had come back to its starting point.
  - Either the test `front_is_clear()` or `wall_in_front()`, and `object_here()`.
  - How to use a `while` or a `repeat/for` loop and an `if` statement.
  - It might be useful to know how to use the negation of a test (`not` in Python).
  - Ideally, you should define your own functions to make your program easier to understand. 
  
  *Hint: Reeborg carries some tokens; you only need to use one.*

A robot located at (x, y) = `(1, 1)` carries **token:500**

---