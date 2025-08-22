# Game 9: Around 3
  
## Around the world  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%203&url=worlds%2Ftutorial_en%2Faround3.json)
[Solution link](around3.py)

Have Reeborg go around the world in the counter-clockwise direction once, and stop at its starting position. Reeborg must not step on the grass. The correct path is shown by the dashed white line. *Hint: Reeborg carries some tokens; you only need to use one.* Your program should also work for world **Around 1** and **Around 2**.

## What you need to know:  
  - The functions `move()`, `turn_left()`, and `put()`.
  - Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `object_here()`.
  - How to use a `while` loop and `if/else` statements.
  - It might be useful to know how to use the negation of a test (`not` in Python).
  - Ideally, you should define your own functions to make your program easier to understand.

A robot located at (x, y) = `(4, 1)` carries **token:infinite number**

## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(4, 1)`

---