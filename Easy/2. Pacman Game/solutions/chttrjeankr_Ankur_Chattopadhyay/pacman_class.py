class PacMan(object):
    """docstring for PacMan."""

    def __init__(self, maze_obj):
        super(PacMan, self).__init__()
        self.pacman_position = (1, 1)
        self.curr_pos = self.pacman_position
        self.maze = maze_obj
        self.last_move = ""

    def move_pacman(self, new_pacman_pos, last_move):
        (
            self.maze.maze_arr[self.curr_pos[0]][self.curr_pos[1]],
            self.maze.maze_arr[new_pacman_pos[0]][new_pacman_pos[1]],
        ) = (" ", "@")
        self.curr_pos = new_pacman_pos
        self.last_move = last_move
