import pandas as pd

import sys
from logger_setup import init_logger

if __name__ == "__main__":
    logger = init_logger()
    try:
        logger.info(f"Starting {sys.argv[0]}")
    except Exception as exception:
        logger.error(exception)
