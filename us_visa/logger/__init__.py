import os
from datetime import datetime

# Function to get the root directory of the project
def get_root_directory():
    return os.path.dirname(os.path.abspath(__file__))

import logging

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = os.path.join(get_root_directory(), 'logs')  # Define the full path to the log directory

# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Construct the path to the log file using the log directory
logs_path = os.path.join(log_dir, LOG_FILE)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
