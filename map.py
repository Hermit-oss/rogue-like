import random
import pygame

class MapGenerator:
    """
    The MapGenerator class generates a floor layout for a game map using an algorithm.

    Attributes:
        width (int): The width of the map.
        height (int): The height of the map.
        min_rooms (int): The minimum number of rooms to be generated.
        max_rooms (int): The maximum number of rooms to be generated.
        map_layout (list): The layout of the map represented as a 2D list of cells.
        rooms (list): A list of created rooms represented as coordinates.

    Methods:
        generate_map(): Generates the map layout using the algorithm.
        _can_create_room(x, y): Checks if a room can be created at the given coordinates.
        _create_room(x, y): Creates a room at the given coordinates and adds it to the rooms list.
        _strip_unnecessary_zeros(): Removes unnecessary rows and columns from the map layout.
        display_map(screen): Displays the map on the provided pygame screen.
        get_map_layout(): Returns the generated map layout.
    """
    def __init__(self, min_rooms, max_rooms):
        """
        Initializes a new instance of the MapGenerator class.

        Parameters:
            min_rooms (int): The minimum number of rooms to be generated. Must be greater than or equal to 1.
            max_rooms (int): The maximum number of rooms to be generated. Must be less than or equal to width * height // 2.

        Note: If min_rooms is bigger than max_rooms, they will switch places.
        """
        self.width = 13
        self.height = 13

        # Set min_rooms to a minimum value of 1
        self.min_rooms = max(min_rooms, 1)

        # Calculate the maximum number of rooms based on the map size
        max_allowed_rooms = self.width * self.height // 2

        # Set max_rooms to a maximum value of max_allowed_rooms
        self.max_rooms = min(max_rooms, max_allowed_rooms)

        # Swap min_rooms and max_rooms if min_rooms is greater than max_rooms
        if self.min_rooms > self.max_rooms:
            self.min_rooms, self.max_rooms = self.max_rooms, self.min_rooms

        self.map_layout = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.rooms = []


    def generate_map(self):
        """
        Generates the map layout using the algorithm.

        The algorithm works as follows:
        1. Find the center of the map.
        2. Create a room at the center and add it to the rooms list.
        3. While the number of created rooms is less than the desired range (randomized):
           4. Choose a room from the rooms list.
           5. Explore the available directions randomly (left, up, right, down).
           6. If a valid direction is found, create a room at the new coordinates and add it to the rooms list.
           7. Repeat steps 4-6 until the desired number of rooms is reached.
        8. Strip unnecessary zeros from the map layout.

        Note: The algorithm ensures that the minimum and maximum room limits are respected.

        """
        center_x = self.width // 2
        center_y = self.height // 2
        self._create_room(center_x, center_y)

        room_count = 1

        while room_count < random.randint(self.min_rooms, self.max_rooms):
            current_room = random.choice(self.rooms)
            x, y = current_room
            directions = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            random.shuffle(directions)

            for direction in directions:
                new_x, new_y = direction
                if self._can_create_room(new_x, new_y):
                    self._create_room(new_x, new_y)
                    room_count += 1
                    break

        self._strip_unnecessary_zeros()

    def _can_create_room(self, x, y):
        """
        Checks if a room can be created at the given coordinates.

        Parameters:
            x (int): The x-coordinate of the room.
            y (int): The y-coordinate of the room.

        Returns:
            bool: True if a room can be created, False otherwise.
        """
        if (
            0 <= x < self.width and
            0 <= y < self.height and
            self.map_layout[y][x] == 0
        ):
            return True
        return False

    def _create_room(self, x, y):
        """
        Creates a room at the given coordinates and adds it to the rooms list.

        Parameters:
            x (int): The x-coordinate of the room.
            y (int): The y-coordinate of the room.
        """
        self.map_layout[y][x] = 1
        self.rooms.append((x, y))

    def _strip_unnecessary_zeros(self):
        """
        Removes unnecessary rows and columns from the map layout.
        """
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
    
    def get_map_layout(self):
        """
        Returns the generated map layout.

        Returns:
            list: A list of lists representing the map layout.
        """
        return self.map_layout

    def display_map(self, screen):
        """
        Displays the map on the provided pygame screen.

        Parameters:
            screen (pygame.Surface): The pygame screen surface to display the map.
        """
        tile_size = 10      # Size of the map squares in pixels
        spacing = 1         # Size of the spacing between squares in pixels
        colors = {
            0: (0, 0, 0),   # Color for 0 (empty) cells
            1: (255, 0, 0), # Color for 1 (room) cells
        }

        map_height = len(self.map_layout)
        map_width = len(self.map_layout[0])

        for y in range(map_height):
            for x in range(map_width):
                if y < len(self.map_layout) and x < len(self.map_layout[y]):
                    cell_color = colors[self.map_layout[y][x]]
                    rect_x = x * (tile_size + spacing)
                    rect_y = y * (tile_size + spacing)
                    pygame.draw.rect(screen, cell_color, (rect_x, rect_y, tile_size, tile_size))