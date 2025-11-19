import logging
import os
from pathlib import Path

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

def get_logger(name: str):
    """Crea y configura un logger con formato estándar del proyecto."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evitar agregar handlers duplicados
    if not logger.handlers:
        file_handler = logging.FileHandler(LOGS_DIR / f"{name}.log", mode="a", encoding="utf-8")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
    