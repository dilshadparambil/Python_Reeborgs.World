# Game 4: Home 4
  
## I want to go home!  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%202&url=worlds%2Ftutorial_en%2Fhome4.json)
[Solution link](home4.py)  

- Write a program that makes Reeborg go home.  
## What you need to know:  
  - The function `move()` and `turn_left().` To make Reeborg **turn right**, you will have to tell it to `turn_left()` three times in a row.
### More Advanced:  
  - You may have noticed that your solution as some repeated patterns as you can see from the image below.  
  - Once you know how to define functions, write a solution with the repeated code put in functions. For example, the yellow shape forms a letter L.
  - This suggest that, we could define two functions, L_shape() and next_L() and use them to solve the problem.
  - Using Python and the special keyword repeat/for unique to Reeborg's World, a solution could be written as:
    ```
    repeat 3:
      L_shape()
      next_L()
    L_shape()
    ```
  - Whereas in traditional Python, it would be written as:  
    ```
    for _ in range(3):
      L_shape()
      next_L()
    L_shape()
    ```
  - If you know how to define functions, you should attempt to write a similar program.  

- A robot located at (x, y) = `(4, 1)` carries no objects  
## Goal to achieve:  
  - The final position of the robot must be (x, y) = `(5, 1)`

---
