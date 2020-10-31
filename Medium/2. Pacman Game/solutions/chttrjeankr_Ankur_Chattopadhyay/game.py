from pacman_class import PacMan
from maze_class import Maze
from ghost_class import Ghost
from utilities import maze as maze_str

maze_obj = Maze(maze_str)
pacman_obj = PacMan(maze_obj)
ghost_obj = Ghost(maze_obj, pacman_obj)

while pacman_obj.is_alive:
    ghost_obj.move_all_ghosts()
    if ghost_obj.ghost_got_pacman:
        # while condition will check is pacman remains alive in next iteration
        continue
    print(maze_obj.get_current_maze())
    print(f"Score: {pacman_obj.pacman_score}")
    try:
        key_press = input("W/S/A/D: ") or pacman_obj.last_move
    except KeyboardInterrupt:
        pacman_obj._end_game()
        continue
    d_pos = maze_obj.get_move(key_press)
    if d_pos:
        new_pacman_pos = maze_obj.get_new_pos(pacman_obj.curr_pos, d_pos)
        valid_move = maze_obj.check_valid_move(new_pacman_pos)
        if valid_move:
            pacman_obj.move_pacman(new_pacman_pos, key_press)
    else:
        print("bad input")
