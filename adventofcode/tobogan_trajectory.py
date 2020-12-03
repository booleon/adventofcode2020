import logging
from pathlib import Path
from typing import List

from adventofcode import read_file


class MapLayer:
    def __init__(self, layer):
        self.layer: str = layer

    @classmethod
    def parse(cls, layer):
        return MapLayer(layer)

    def is_tree_on_position(self, position: int) -> bool:
        relative_position = position % len(self.layer)
        return self.layer[relative_position - 1] == "#"


class Map:
    def __init__(self, layers: List[MapLayer]):
        self.layers = layers
        self.current_layer = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_layer = self.current_layer
        self.current_layer += 1
        try:
            return self.layers[current_layer]
        except IndexError:
            raise StopIteration

    def __len__(self):
        return len(self.layers)

    @classmethod
    def parse(cls, raw_map: List[str]):
        layers = [MapLayer(layer) for layer in raw_map]
        return Map(layers)


class Tobogan:
    def __init__(self, right: int, down: int):
        self.right = right
        self.down = down

    def get_encounter_trees_on(self, airport_map: Map):
        encounter_trees = 0
        next_position = Position(1, 1)
        current_position = Position(0, 0)

        for layer in airport_map:
            current_position = Position(right=next_position.right, down=current_position.down)
            current_position = current_position.move_down(1)

            if current_position.down != next_position.down:
                continue

            encounter_trees = self._update_encounter_trees(current_position, encounter_trees, layer)
            next_position = current_position.move_right(self.right).move_down(self.down)

        return encounter_trees

    @staticmethod
    def _update_encounter_trees(current_position, encounter_trees, layer):
        if layer.is_tree_on_position(current_position.right):
            encounter_trees += 1
        return encounter_trees


class Position:
    def __init__(self, right: int, down: int):
        self.down = down
        self.right = right

    def move_down(self, step: int):
        return Position(self.right, self.down + step)

    def move_right(self, step: int):
        return Position(self.right + step, self.down)


def main():
    file_path = Path('.') / "advent_data_tobogan"
    lines = read_file(file_path)
    logging.info(f"d3e1")
    print(Tobogan(3, 1).get_encounter_trees_on(Map.parse(lines)))
    logging.info(f"d3e2")
    case1 = Tobogan(1, 1).get_encounter_trees_on(Map.parse(lines))
    logging.info(case1)
    case2 = Tobogan(3, 1).get_encounter_trees_on(Map.parse(lines))
    logging.info(case2)
    case3 = Tobogan(5, 1).get_encounter_trees_on(Map.parse(lines))
    logging.info(case3)
    case4 = Tobogan(7, 1).get_encounter_trees_on(Map.parse(lines))
    logging.info(case4)
    case5 = Tobogan(1, 2).get_encounter_trees_on(Map.parse(lines))
    logging.info(case5)
    print(case1 * case2 * case3 * case4 * case5)
