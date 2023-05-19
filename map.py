import random

class MapGenerator:
    def __init__(self, min_rooms, max_rooms):
        self.width = 13
        self.height = 13
        self.min_rooms = min_rooms
        self.max_rooms = max_rooms
        self.map_layout = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def generate_map(self):
        center_x = self.width // 2
        center_y = self.height // 2
        self.map_layout[center_y][center_x] = 1

        working_x = center_x
        working_y = center_y

        room_count = 1

        while room_count < random.randint(self.min_rooms, self.max_rooms):
            if self._check_and_create_room(working_x - 1, working_y):
                working_x -= 1
                room_count += 1
            elif self._check_and_create_room(working_x, working_y - 1):
                working_y -= 1
                room_count += 1
            elif self._check_and_create_room(working_x + 1, working_y):
                working_x += 1
                room_count += 1
            elif self._check_and_create_room(working_x, working_y + 1):
                working_y += 1
                room_count += 1
            else:
                working_x = center_x
                working_y = center_y

        self._strip_unnecessary_zeros()

    def _check_and_create_room(self, x, y):
        if (
            0 <= x < self.width and
            0 <= y < self.height and
            self.map_layout[y][x] == 0 and
            random.randint(1, 2) % 2 == 0
        ):
            self.map_layout[y][x] = 1
            return True
        return False

    def _strip_unnecessary_zeros(self):
        first_col = next(
            (col for col in range(self.width) if any(row[col] for row in self.map_layout)),
            0
        )
        last_col = next(
            (col for col in range(self.width - 1, -1, -1) if any(row[col] for row in self.map_layout)),
            self.width - 1
        )
        first_row = next(
            (row for row in range(self.height) if any(self.map_layout[row])),
            0
        )
        last_row = next(
            (row for row in range(self.height - 1, -1, -1) if any(self.map_layout[row])),
            self.height - 1
        )

        self.map_layout = [
            row[first_col:last_col + 1]
            for row in self.map_layout[first_row:last_row + 1]
        ]

    def print_map(self):
        for row in self.map_layout:
            print(' '.join(str(cell) for cell in row))