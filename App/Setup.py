from App.Project_Logger import Console_and_file_logger
import os

import logging

logger = Console_and_file_logger(os.path.basename(__file__))