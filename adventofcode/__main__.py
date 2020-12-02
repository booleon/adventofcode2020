import logging
from pathlib import Path

from adventofcode import expense
from adventofcode.password import count_valid_passwords

logging.basicConfig(level=logging.INFO)


def read_file(local_file_path):
    local_file_path.resolve()
    logging.info(f"filepath is : {file_path.as_posix()}")
    with local_file_path.open() as file:
        return [line.rstrip() for line in file]


#######
logging.info("start file")
file_path = Path('.') / "advent_data_expense"
lines = [int(line) for line in read_file(file_path)]
expense.main(lines)
########

file_path = Path('.') / "advent_data_passwords"
lines = read_file(file_path)
logging.info(f"d1e1")
print(count_valid_passwords(lines))
