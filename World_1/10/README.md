# Game 10: Around 4
  
## Around the world  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%204&url=worlds%2Ftutorial_en%2Faround4.json)  
[Solution link](around4.py)

Have Reeborg go around the world in the counter-clockwise direction once, and stop at its starting position. Reeborg must not step on the grass. The correct path is shown by the dashed white line. *Hint: Reeborg carries some tokens; you only need to use one.* Your program should also work for worlds **Around 1**, **Around 2**, and **Around 3**.

## What you need to know:  
  - The functions `move()`, `turn_left()`, and `put()`.
  - Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `object_here()`.
  - How to use a `while` loop and `if/elif/else` statements.
  - It might be useful to know how to use the negation of a test (`not` in Python).
  - Ideally, you should define your own functions to make your program easier to understand.

A robot located at (x, y) = `(4, 1)` carries **token:infinite number**

## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(4, 1)`
