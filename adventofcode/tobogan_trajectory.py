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

    @classmethod
    def parse(cls, raw_map: List[str]):
        layers = [MapLayer(layer) for layer in raw_map]
        return Map(layers)


class Tobogan(object):
    @classmethod
    def get_encounter_trees_on(cls, airport_map: Map):
        encounter_trees = 0
        position = 1
        for layer in airport_map:
            if layer.is_tree_on_position(position):
                encounter_trees += 1
            position += 3
        return encounter_trees


def main():
    file_path = Path('.') / "advent_data_tobogan"
    lines = read_file(file_path)
    logging.info(f"d3e1")
    road_to_airport_map = Map.parse(lines)
    print(Tobogan.get_encounter_trees_on(road_to_airport_map))
