"""Logging configuration using Loguru."""

import sys
from loguru import logger
from app.core.config import settings


def setup_logging():
    """Configure Loguru for structured logging."""

    # Remove default handler
    logger.remove()

    # Add console handler with color and formatting
    logger.add(
        sys.stdout,
        format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=settings.log_level,
        colorize=True,
    )

    # Add file handler if in production or specified
    if settings.environment != "test":
        logger.add(
            settings.log_file,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
            level=settings.log_level,
            rotation="500 MB",  # Rotate log file every 500MB
            retention="7 days",  # Keep logs for 7 days
        )

    return logger


# Initialize logger on module load
logger_instance = setup_logging()
