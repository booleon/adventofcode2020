import pytest

from adventofcode.tobogan_trajectory import MapLayer, Map, Tobogan


class TestMapLayer:
    class TestIsTreeOnPosition:
        def test_given_no_tree(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            layer = "..##......."
            # act
            result = MapLayer.parse(layer).is_tree_on_position(1)

            # assert
            assert result is False

        def test_given_tree(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            layer = "..##......."
            # act
            result = MapLayer.parse(layer).is_tree_on_position(3)

            # assert
            assert result is True

        def test_given_loop(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            layer = "..#"
            # act
            result = MapLayer.parse(layer).is_tree_on_position(6)

            # assert
            assert result is True

        def test_given_big_loop(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            layer = "..#"
            # act
            result = MapLayer.parse(layer).is_tree_on_position(30)

            # assert
            assert result is True


class TestMap:
    class TestParse:
        def test_given(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            first_layer = "..##......."
            second_layer = "#...#...#.."
            third_layer = ".#....#..#."
            raw_map = [first_layer, second_layer, third_layer]

            # act
            result = Map.parse(raw_map)

            # assert
            assert next(result).layer == first_layer
            assert next(result).layer == second_layer
            assert next(result).layer == third_layer
            with pytest.raises(StopIteration):
                assert next(result).layer


class TestTobogan:
    class TestGetEncounteredTrees:
        def test_given(self):
            """
            Given:
            When:
            Then:
            """
            # arrange

            layers = [
                "..##.......",
                "#...#...#..",
                ".#....#..#.",
                "..#.#...#.#",
                ".#...##..#.",
                "..#.##.....",
                ".#.#.#....#",
                ".#........#",
                "#.##...#...",
                "#...##....#",
                ".#..#...#.#"]
            road_to_airport_map = Map.parse(layers)
            # act
            result = Tobogan.get_encounter_trees_on(road_to_airport_map)

            # assert
            assert result == 7
