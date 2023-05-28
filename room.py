from tile import TileMap, Tile, enemy_class

class Room:
    def __init__(self, tile_map):
        self.tile_map = tile_map

    def draw(self, screen):
        for row in self.tile_map.tiles:
            for tile in row:
                tile.draw(screen)
        self.tile_map.enemies.display_enemy(screen)
