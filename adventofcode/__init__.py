__version__ = '0.1.0'

import logging

logging.basicConfig(level=logging.INFO)


def read_file(local_file_path):
    local_file_path.resolve()
    logging.info(f"filepath is : {local_file_path.as_posix()}")
    with local_file_path.open() as file:
        return [line.rstrip() for line in file]
