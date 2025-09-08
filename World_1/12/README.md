# Game 12: Center 2  

## Find the center  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Center%202&url=worlds%2Ftutorial_en%2Fcenter2.json)  
[Solution link](center2.py)

Help Reeborg to find the center of the world. The height and width of the world will change each time, but they each will be an odd number, from 1 to 11.  

Make sure to have a working program for the world **Center 1** first.

## What you need to know:  
  - The functions `move()`, `turn_left()` and `put()`.  
  - The conditions `front_is_clear()` or `wall_in_front()`, and `object_here()`.  
  - How to use `while` loops and `if` statements.  

## Suggested strategy:  
Find a way to use twice the strategy you used for solving world **Center 1**. Knowing how to use the condition `is_facing_north()`, could help you to simplify slightly your program.  

A robot located at (x, y) = `(1, 1)` carries **token:200**

## Goal to achieve:  
  - Reeborg must stop and mark the **center** of the world.
