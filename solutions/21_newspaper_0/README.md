# Game 21: Newspaper 0  

## Newspaper delivery  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Newspaper%200&url=worlds%2Ftutorial_en%2Fnewspaper0.json)  
[Solution link](newspaper0.py)

Reeborg must deliver the newspaper **The Northern Star**. To do this, Reeborg must:  
1. Take the newspaper using `take()`.  
2. Climb up three steps.  
3. Put down the newspaper using `put()`.  
4. Return to its starting point.  

## What you need to know:  
  - The functions `move()`, `turn_left()`, `take()`, and `put()`.  

### For more advanced students  
If you know how to define functions, create helper functions so your program can be run as follows:  

```python
take()
up_three_steps()
put()
turn_around()
down_three_steps()
```

You should also define other helper functions such as `turn_right()`, `up_one_step()`, etc., to avoid code repetition

A robot located at (x, y) = `(1, 1)` carries **no objects**  

## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(1, 1)`