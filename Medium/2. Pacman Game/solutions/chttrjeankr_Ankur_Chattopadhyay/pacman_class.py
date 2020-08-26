class PacMan(object):
    """docstring for PacMan."""

    def __init__(self, maze_obj):
        super(PacMan, self).__init__()
        self.pacman_position = (1, 1)
        self.curr_pos = self.pacman_position
        self.maze = maze_obj
        self.last_move = str()
        self.pacman_score = 0
        self._points_per_dot = 5
        self.is_alive = True

    def move_pacman(self, new_pacman_pos, last_move):
        if (
            self.maze.maze_arr[new_pacman_pos[0]][new_pacman_pos[1]]
            == self.maze._ghost_char
        ):
            (
                self.maze.maze_arr[self.curr_pos[0]][self.curr_pos[1]],
                self.maze.maze_arr[new_pacman_pos[0]][new_pacman_pos[1]],
            ) = (self.maze._space_char, self.maze._dead_pacman_char)
            self._end_game()
        self.calc_score(new_pacman_pos)
        (
            self.maze.maze_arr[self.curr_pos[0]][self.curr_pos[1]],
            self.maze.maze_arr[new_pacman_pos[0]][new_pacman_pos[1]],
        ) = (self.maze._space_char, self.maze._pacman_char)
        self.curr_pos = new_pacman_pos
        self.last_move = last_move
        if self.maze.left_dots == 0:
            self._end_game()

    def calc_score(self, new_pacman_pos):
        if (
            self.maze.maze_arr[new_pacman_pos[0]][new_pacman_pos[1]]
            == self.maze._point_char
        ):
            self.pacman_score += self._points_per_dot
            self.maze.left_dots -= 1

    def _end_game(self):
        self.is_alive = False
        print(self.maze.get_current_maze())
        print("\nEND OF GAME")
        print(f"Final Score: {self.pacman_score}")
