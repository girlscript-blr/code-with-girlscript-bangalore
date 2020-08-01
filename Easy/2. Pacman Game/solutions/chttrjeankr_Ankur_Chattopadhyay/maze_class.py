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
        self.maze_arr = self._maze_array(maze)

    def get_move(self, key_press):
        try:
            reqd_key = filter(
                lambda k: key_press in k, self.mapping_keys.keys()
            ).__next__()
        except StopIteration:
            return None
        move = self.mapping_keys[reqd_key]
        return self.directions.get(move)

    def _maze_array(self, maze_str):
        res_list = []
        rows = maze_str.split("\n")[1:-1]
        for row in rows:
            res_list.append(list(row))
        return res_list

    def get_current_maze(self):
        return "\n".join(("".join(row) for row in self.maze_arr))

    def get_new_pos(self, pos, d_pos):
        xi, yi = pos
        dx, dy = d_pos
        return (xi + dx, yi + dy)

    def check_valid_move(self, new_pacman_pos):
        xf, yf = new_pacman_pos
        return self.maze_arr[xf][yf] in [" "]
