# EASY PACMAN

## Simulation

> ![Peek 2020-08-01 23-27](https://user-images.githubusercontent.com/39518771/89107467-dc7df000-d44e-11ea-9da7-b321b60fab35.gif)

## Approach

1. A static maze is created using a readabale, easily editable string in `utilities.maze`. This string is automatically converted to a 2D array when playing the game.
2. `Maze` class handles the characteristics of the maze, converts inputs into valid movements and validates new positions.
3. `PacMan` class handles the movement of `PacMan` in the `Maze`.
4. `game.py` has the code which creates the `PacMan` and `Maze` objects and handles inputs from user. It prints the current maze after each input.
5. Available keys are W,S,A,D; and the last key press is repeated when blank input is provided.

## Usage

Make sure you're in the right directory:

```
code-with-girlscript-bangalore/Easy/2. Pacman Game/solutions/chttrjeankr_Ankur_Chattopadhyay/
```

To start game, execute:

```
python game.py
```
