class Maze(object):
    """docstring for Maze."""

    def __init__(self, maze):
        super(Maze, self).__init__()
        self.directions = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        self.mapping_keys = {
            "Ww": "up",
            "Ss": "down",
            "Aa": "left",
            "Dd": "right",
        }
        self.reverses = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left",
        }
        self.left_dots = 0
        self._space_char = " "
        self._point_char = "."
        self._ghost_char = "&"
        self._pacman_char = "@"
        self._dead_pacman_char = "X"
        self._horz_wall_char = "-"
        self._vert_wall_char = "|"
        self.allowed_for_pacman = [
            self._space_char,
            self._point_char,
            self._ghost_char,
        ]
        self.allowed_for_ghosts = [
            self._space_char,
            self._point_char,
            self._pacman_char,
        ]
        self.maze_arr = self._make_maze_array(maze)

    def get_move(self, key_press):
        try:
            reqd_key = filter(
                lambda k: key_press in k, self.mapping_keys.keys()
            ).__next__()
        except StopIteration:
            return None
        move = self.mapping_keys[reqd_key]
        return self.directions.get(move)

    def get_move_arrows(self, arrow):
        return self.directions.get(arrow)

    def _make_maze_array(self, maze_str):
        res_list = []
        points = 0
        rows = maze_str.split("\n")[1:-1]
        for row in rows:
            points += row.count(self._point_char)
            res_list.append(list(row))
        self.left_dots = points
        return res_list

    def get_current_maze(self):
        return "\n" + "\n".join(("".join(row) for row in self.maze_arr))

    def get_new_pos(self, pos, d_pos):
        xi, yi = pos
        dx, dy = d_pos
        return (xi + dx, yi + dy)

    def check_valid_move(self, new_pacman_pos):
        xf, yf = new_pacman_pos
        return self.maze_arr[xf][yf] in self.allowed_for_pacman

    def check_ghost_move(self, new_ghost_pos):
        xf, yf = new_ghost_pos
        return self.maze_arr[xf][yf] in self.allowed_for_ghosts

    def get_random_direction(self):
        from random import choice as rnd_choice

        return rnd_choice(list(self.directions.values()))

    def get_reverse_direction(self, ini_dir):
        return (ini_dir[0] * -1, ini_dir[1] * -1)
