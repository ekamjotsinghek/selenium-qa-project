import logging
import os
from datetime import datetime

def get_logger(name):
    # Create logs folder if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    # Create unique log filename with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"logs/test_run_{timestamp}.log"

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # File handler — saves logs to file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Console handler — shows logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format — what each log line looks like
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger