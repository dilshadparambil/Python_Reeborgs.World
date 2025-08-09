# 🤖 Reborg's world challenge

[Reeborg's World Chanllenge](https://reeborg.ca/reeborg.html) is intended to help beginners to learn programming, using Python (Javascript is also supported).  
You should have a look at the [documentation](https://reeborg.ca/docs/en/), which includes a programming tutorial to find out more about it.  

Reborg's World website: [click here](https://reeborg.ca/index_en.html)

---

## 📅 Table of Contents

| S.No | Challenge Title  | Goto                          | Solution                    |
|------|------------------|-------------------------------|-----------------------------|
| 1    | Home 1           | [Game 1](#game-1-home-1)      |[link](solutions/home1.py)   |
| 2    | Home 2           | [Game 2](#game-2-home-2)      |[link](solutions/home2.py)   |
| 3    | Home 3           | [Game 3](#game-3-home-3)      |[link](solutions/home3.py)   |
| 4    | Home 4           | [Game 4](#game-4-home-4)      |[link](solutions/home4.py)   |


---

### Game 1: Home 1
  
#### I want to go home!  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%201&url=worlds%2Ftutorial_en%2Fhome1.json)

- Write a program that makes Reeborg go home.  
- **What you need to know:** The function `move().`
- A robot located at (x, y) = (3, 1) carries no objects.
- **Goal to achieve:** The final position of the robot must be (x, y) = (1, 1)

---

### Game 2: Home 2
  
#### I want to go home!  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%202&url=worlds%2Ftutorial_en%2Fhome2.json)
- Write a program that makes Reeborg go home.  
- **What you need to know:** The function `move().`
- A robot located at (x, y) = (1, 3) carries no objects.
- **Goal to achieve:** The final position of the robot must be (x, y) = (1, 1)

---

### Game 3: Home 3
  
#### I want to go home!  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%202&url=worlds%2Ftutorial_en%2Fhome3.json)
- Write a program that makes Reeborg go home.  
- **What you need to know:** The function `move()` and `turn_left().`
- A robot located at (x, y) = (1, 3) carries no objects.
- **Goal to achieve:** The final position of the robot must be (x, y) = (2, 1)

---

### Game 4: Home 4
  
#### I want to go home!  
[Game Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%202&url=worlds%2Ftutorial_en%2Fhome4.json)
- Write a program that makes Reeborg go home.  
- **What you need to know:** The function `move()` and `turn_left().` To make Reeborg turn right, you will have to tell it to `turn_left()` three times in a row.
- **More Advanced**:  
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
    - Whereas in traditional Python, it would be written as:  ```
      ```
      for _ in range(3):
        L_shape()
        next_L()
      L_shape()
      ```
    - If you know how to define functions, you should attempt to write a similar program.
- A robot located at (x, y) = (4, 1) carries no objects. 
- **Goal to achieve:** The final position of the robot must be (x, y) = (5, 1)

---

