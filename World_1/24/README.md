# Game 24: Rain 1  

## Rain is falling.  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Rain%201&url=worlds%2Ftutorial_en%2Frain1.json)  
[Solution link](rain1.py)

It's raining hard. Water is going to come in through the **open windows**, so Reeborg must close them.  

Have Reeborg:  
1. Move around the room.  
2. Close all open windows by using the `build_wall()` function.  

In this world, **the size of the room and window locations always change**.  

## What you need to know:  
  - The functions `move()`, `turn_left()`, and `build_wall()`.  
  - The conditions `right_is_clear()` or `wall_on_right()`, and `at_goal()`.  
  - How to use a `while` loop and an `if` statement.  
  - Windows (missing walls) are always between two walls along a single line.  
  - There can never be **two windows side by side**, nor a **window at a corner**.  

A robot located at (x, y) = `(4, 5)` carries **no objects**  

## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(4, 5)`
