# Game 25: Rain 2  

## Rain is falling.  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Rain%202&url=worlds%2Ftutorial_en%2Frain2.json)  
[Solution link](rain2.py)

It's raining hard. Water is going to come in through the **open windows**, so Reeborg must close them.  

Have Reeborg:  
1. Move around the room.  
2. Close all open windows using the `build_wall()` function.  

In this world, **the shape and size of the room, and the window locations change every time**.  
Your program should also work for **Rain 1**.  

> 💡 *Hint*: Imagine Reeborg is standing next to a wall, takes a single step, and finds there’s no wall next to him anymore. What can happen if he takes another step? There are **two possible cases** to consider.  

## What you need to know:  
  - The functions `move()`, `turn_left()`, and `build_wall()`.  
  - The conditions `right_is_clear()` or `wall_on_right()`, and `at_goal()`.  
  - How to use a `while` loop and an `if` statement.  
  - Windows (missing walls) are always between two walls along a straight line.  
  - There can never be **two windows side by side**, nor a **window at a corner**.  

A robot located at (x, y) = `(4, 7)` carries **no objects**  

## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(4, 6)`
