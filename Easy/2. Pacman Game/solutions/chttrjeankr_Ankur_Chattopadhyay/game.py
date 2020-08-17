from pacman_class import PacMan
from maze_class import Maze
from utilities import maze as maze_str

maze_obj = Maze(maze_str)
pacman_obj = PacMan(maze_obj)

while True:
    print(maze_obj.get_current_maze())
    try:
        key_press = input("W/S/A/D: ") or pacman_obj.last_move
    except KeyboardInterrupt:
        print("\nEND OF GAME")
        break
    d_pos = maze_obj.get_move(key_press)
    if d_pos:
        new_pacman_pos = maze_obj.get_new_pos(pacman_obj.curr_pos, d_pos)
        valid_move = maze_obj.check_valid_move(new_pacman_pos)
        if valid_move:
            pacman_obj.move_pacman(new_pacman_pos, key_press)
    else:
        print("bad input")
