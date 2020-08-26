# MEDIUM PACMAN

## Simulation

> ![Peek 2020-08-26 11-16](https://user-images.githubusercontent.com/39518771/91265507-8884d380-e78e-11ea-8e7d-7be7a04acd97.gif)

## Approach

1. A static maze is created using a readabale, easily editable string in `utilities.maze`. This string is automatically converted to a 2D array when playing the game.
2. `Maze` class handles the characteristics of the maze, converts inputs into valid movements and validates new positions.
3. `PacMan` class handles the movement of `PacMan` in the `Maze`.
4. `Ghost` class handles the random movement of `Ghost` around the `Maze`.
5. `game.py` has the code which creates the `PacMan` and `Maze` objects, randomizes ghosts and handles inputs from user. It prints the current maze before each input, until thr game ends.
6. The game ends when pacman meets ghost or all the points are collected.
7. Available keys are W,S,A,D; and the last key press is repeated when blank input is provided.

## Usage

Make sure you're in the right directory:

```
code-with-girlscript-bangalore/Medium/2. Pacman Game/solutions/chttrjeankr_Ankur_Chattopadhyay/
```

To start game, execute:

```
python game.py
```
