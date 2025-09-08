# Game 20: Maze  

## Lost in a maze  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)  
[Solution link](maze.py)

Reeborg was exploring a dark maze and the battery in its flashlight ran out.  

Write a program using an `if/elif/else` statement so Reeborg can find the exit. The secret is to have Reeborg **follow along the right edge of the maze**:  
- Turn **right** if possible,  
- Go **straight ahead** if it can’t turn right,  
- Turn **left** as a last resort.  

## What you need to know:  
  - The functions `move()` and `turn_left()`.  
  - Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `at_goal()`.  
  - How to use a `while` loop and `if/elif/else` statements.  
  - It might be useful to know how to use the **negation of a test** (`not` in Python).  

A robot located at (x, y) = `(5, 4)` carries **no objects**  

## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(6, 4)`
