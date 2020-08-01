# Pacman Game - Hard

> Date : 1st August 2020

## Prerequisites
- Basic data manipulation in two dimentional array / matrix.
  - https://beginnersbook.com/2014/01/2d-arrays-in-c-example
- How to use keyboard's arrow keys as input.
  - For C/C++:
    - https://www.researchgate.net/post/How_to_use_arrow_keys_in_c_programming_language
    - http://cprogrampracticals.blogspot.com/2016/04/c-program-to-use-arrow-keys.html
  - For Python:
    - https://pythonhosted.org/pynput/keyboard.html
    - https://www.geeksforgeeks.org/python-drawing-design-using-arrow-keys-in-pygame/
  - for JavaScript:
    - https://www.geeksforgeeks.org/javascript-detecting-the-pressed-arrow-key/

## Problem Statement

All of us would have played the famous ‘PACMAN GAME’ in our childhood. 😃 The time has come to write code 👨‍💻👩‍💻 for the same!
The objective of the problem is to allow the Pacman to move along the walls of the maze.
In this section, the Pacman needs to collect the ‘points’ as it moves in the maze. The pacman will also have the ‘ghost’ as its opponent. In addition to this, different levels (atleast 3) of the maze structure should be created and stored in the database. The message “You won” should be displayed on completion of all the levels. The code written should satisfy the requirements given below.

- Create a static 2D array that will represent a maze. There should be 3 types of characters stored in the 2D array.
  - One will represent a horizontal wall. (Ex: ‘-’)
  - One will represent a vertical wall. (Ex: ‘|’)
  - One will represent blank space. (Ex: ‘ ’)
  - One to represent the Pacman. (Ex: ‘@’)
  - Character to represent points that Pacman can collect. (Ex: ‘.’)
  - One to represent a ghost. (Ex: ‘&’)
  - Example <br> ![Example image](../../assets/images/pacmanGameHard.png)

- Store this maze structure in a file or in the database.
- Similarly, create different levels. (At least 3)
- Each must have a minimum of 10 rows and 40 columns.
- When the app runs, the maze should be displayed along with the horizontal & vertical walls, blank space, ghosts, and the Pacman.
- When the arrow keys are pressed the Pacman should move in the respective direction. (The Pacman obviously cannot move through the walls)
- When the Pacman and ghost collide, the game should end. 
- The initial score should be zero and displayed at the bottom or top of the maze (outside the maze). 
- When the Pacman lands on a point character, the point character should be removed and 5 points should be added to the player score.
- The ghost should move automatically. The movement algorithm can be created by considering the following points:
  - The ghost should start moving in a random direction (left, right, up or down) and continue to move until it hits a wall.
  - After hitting the wall the direction of movement of that ghost should change to a random direction.
- The game should end after all the points have been collected and move on to the next level.
- After the last level is completed “Congratulations, You Won!” should be displayed.

### Inputs

The user should be able to control the pacman with arrow keys, or (W,A,S,D).

### Output

The maze should be displayed on the screen and the player should be able to control the pacman. Once first level is completed it should redirect to the next till all levels are completed.

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `30th August 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Stuck somewhere?

Then you might want to solve these versions of the problem first.

- [Easy](../../Easy/2.%20Pacman%20Game/README.md)
- [Medium](../../Medium/2.%20Pacman%20Game/README.md)
