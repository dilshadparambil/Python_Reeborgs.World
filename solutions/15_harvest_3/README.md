# Game 15: Harvest 3  

## Planting time  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Harvest%203&url=worlds%2Ftutorial_en%2Fharvest3.json)  
[Solution link](harvest3.py)

Reeborg has planted some carrot seeds. At some places no carrot has grown; at others, many carrots are growing.  

Have Reeborg remove the excess carrots and plant new ones where there is none so that there is only **one carrot at each location**. Reeborg already carries enough carrots (seeds) to replant the entire garden if needed.  

## What you need to know:  
  - The functions `move()`, `turn_left()`, `put()` and `take()`.  
  - The test `object_here()`.  
  - How to use a `while` loop.  
  - You might find it convenient to define a function named `fix_one_row()` and call this function 6 times.  

A robot located at (x, y) = `(1, 1)` carries **carrot:36**  

## Goal to achieve:  
  - Reeborg must ensure **exactly one carrot** is present at every garden location.
