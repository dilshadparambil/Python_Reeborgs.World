# Game 11: Center 1  

## Find the center  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Center%201&url=worlds%2Ftutorial_en%2Fcenter1.json)  
[Solution link](center1.py)

Help Reeborg to find the center of the world. The height of the world will always be equal to 1 but the width is an odd number which will vary between 3 to 11.

## What you need to know:  
  - The functions `move()`, `turn_left()` and `put()`.  
  - The conditions `front_is_clear()` or `wall_in_front()`, and `object_here()`.  
  - How to use `while` loops and `if` statements.  

## Suggested strategy:  
Reeborg carries many tokens. A possible strategy is to only use two tokens and put one at each end of the world. Then, by moving them one step at a time, Reeborg could find the center of the world.

A robot located at (x, y) = `(1, 1)` carries **token:200**

## Goal to achieve:  
  - Reeborg must stop and mark the **center** of the world.
