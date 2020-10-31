class Ghost(object):
    """docstring for Ghost."""

    def __init__(self, maze_obj, pacman_obj):
        super(Ghost, self).__init__()
        self.maze = maze_obj
        self.ghost_positions = list()
        self.ghost_directions = list()
        self.last_ele_bef_ghost = dict()
        self.pacman = pacman_obj
        self.ghost_got_pacman = False
        self.get_all_ghosts()

    def get_all_ghosts(self):
        for i, row in enumerate(self.maze.maze_arr):
            for j, ele in enumerate(row):
                if ele == self.maze._ghost_char:
                    self.ghost_positions.append((i, j))
        self.ghost_directions = [
            self.maze.get_random_direction() for _ in range(self.no_of_ghosts)
        ]

    @property
    def no_of_ghosts(self):
        return len(self.ghost_positions)

    def move_all_ghosts(self):
        for ghost_i in range(self.no_of_ghosts):
            if not self.ghost_got_pacman:
                self.move_ghost(ghost_i)
            else:
                # to not move remaining ghosts once pacman gets eaten by any one
                break

    def move_ghost(self, ghost_i):
        ghost_position = self.ghost_positions[ghost_i]
        ghost_d_pos = self.ghost_directions[ghost_i]
        new_ghost_pos = self.maze.get_new_pos(ghost_position, ghost_d_pos)
        valid_move = self.maze.check_ghost_move(new_ghost_pos)
        if valid_move:
            try:
                last_ele = self.last_ele_bef_ghost[ghost_position]
                del self.last_ele_bef_ghost[ghost_position]
            except KeyError:
                last_ele = " "
            # fmt: off
            self.last_ele_bef_ghost[new_ghost_pos] = \
                self.maze.maze_arr[new_ghost_pos[0]][new_ghost_pos[1]]
            # fmt: on

            if (
                self.maze.maze_arr[new_ghost_pos[0]][new_ghost_pos[1]]
                == self.maze._pacman_char
            ):
                (
                    self.maze.maze_arr[ghost_position[0]][ghost_position[1]],
                    self.maze.maze_arr[new_ghost_pos[0]][new_ghost_pos[1]],
                ) = (
                    last_ele,
                    self.maze._dead_pacman_char,
                )
                self.pacman._end_game()
                self.ghost_got_pacman = True
            else:
                (
                    self.maze.maze_arr[ghost_position[0]][ghost_position[1]],
                    self.maze.maze_arr[new_ghost_pos[0]][new_ghost_pos[1]],
                ) = (
                    last_ele,
                    self.maze._ghost_char,
                )
            self.ghost_positions[ghost_i] = new_ghost_pos
        else:
            # once blocked, change in random direction
            self.ghost_directions[ghost_i] = self.maze.get_random_direction()
