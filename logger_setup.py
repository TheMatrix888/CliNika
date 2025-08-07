from loguru import logger
from datetime import datetime
from pathlib import Path
import sys


def init_logger(logs_folder: str = "logs", log_level_file: str = "DEBUG", log_level_console: str = "INFO"):
    now = datetime.now()

    logger.remove()  # Remove default settings

    # Create logs folder if didn't find one
    logs_dir = Path(logs_folder)
    logs_dir.mkdir(exist_ok=True)

    # File path
    timestamp = now.strftime("%d-%m-%Y")
    log_path = logs_dir / f"{timestamp}.log"

    # File loger
    logger.add(
        log_path,
        level=log_level_file
    )

    # Console loger
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
        level=log_level_console
    )

    return logger
