from loguru import logger
import sys

# Remove the default logger to prevent duplicate logging
logger.remove()

# Add a new handler with the desired format
logger.add(
    sys.stderr,  # Use sys.stderr to output logs to the console
    format="{level} | {message}"
)

from .decorator import all_methods_logger