import logging
import os
from datetime import datetime

class Logger:
    log_directory = "logs"
    log_filename = f"test_log_{datetime.now().strftime('%Y-%m-%d')}.log"
    log_path = os.path.join(log_directory, log_filename)

    @staticmethod
    def setup_logger():
        if not os.path.exists(Logger.log_directory):
            os.makedirs(Logger.log_directory)

        logging.basicConfig(
            filename=Logger.log_path,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filemode="a",
            force=True
        )

        logger = logging.getLogger()
        logger.addHandler(logging.StreamHandler())  # Logs to console as well
        return logger

logger = Logger.setup_logger()
