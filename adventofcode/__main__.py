import logging
from pathlib import Path

from adventofcode import expense, tobogan_trajectory, read_file
from adventofcode.password import count_sled_valid_passwords, count_tobogan_valid_passwords
from adventofcode.tobogan_trajectory import Tobogan, Map

#######
logging.info("start file")
file_path = Path('.') / "advent_data_expense"
lines = [int(line) for line in read_file(file_path)]
expense.main(lines)
########

file_path = Path('.') / "advent_data_passwords"
lines = read_file(file_path)
logging.info(f"d2e1")
print(count_sled_valid_passwords(lines))
logging.info(f"d2e2")
print(count_tobogan_valid_passwords(lines))

tobogan_trajectory.main()
