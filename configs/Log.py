import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)