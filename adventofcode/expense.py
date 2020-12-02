import logging
from typing import List


def is_equal_to_2020(*entries):
    return sum(entries) == 2020


def get_number_summing_2020(entries: list):
    local_entries = entries[:]
    potential_result = []
    while local_entries and not potential_result:
        first_number = local_entries.pop(0)
        potential_result = _get_missing_number_to_2020((first_number,), local_entries)
    return potential_result


def get_3_number_summing_2020(entries: list):
    local_entries = entries[:]
    potential_result = ()
    while len(local_entries) > 2 and not potential_result:
        first_number = local_entries.pop(0)
        local_insider = local_entries[:]
        while local_insider and not potential_result:
            second_number = local_insider.pop(0)
            potential_result = _get_missing_number_to_2020((first_number, second_number), local_insider)
    return potential_result


def _get_missing_number_to_2020(fist_items: tuple, entries: List[int]) -> tuple:
    potential_result = [(fist_items + (other_number,))
                        for other_number in entries
                        if is_equal_to_2020(other_number, *fist_items)
                        ]
    if potential_result:
        return potential_result[0]
    return ()


def main(lines: list):
    logging.info(f"d1e1")
    numbers = get_number_summing_2020(lines)
    print(numbers[0] * numbers[1])
    logging.info(f"d1e1")
    numbers3 = get_3_number_summing_2020(lines)
    print(numbers3[0] * numbers3[1] * numbers3[2])