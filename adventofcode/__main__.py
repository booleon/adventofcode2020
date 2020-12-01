import logging
from pathlib import Path

from adventofcode.expense import get_number_summing_2020, get_3_number_summing_2020

logging.basicConfig(level=logging.INFO)

logging.info("start file")

file_path = Path('.') / "advent_data"
file_path.resolve()
logging.info(f"filepath is : {file_path.as_posix()}")

with file_path.open() as file:
    lines = [int(line.rstrip()) for line in file]

numbers = get_number_summing_2020(lines)
print(numbers[0] * numbers[1])

numbers3 = get_3_number_summing_2020(lines)
print(numbers3[0] * numbers3[1] * numbers3[2])

