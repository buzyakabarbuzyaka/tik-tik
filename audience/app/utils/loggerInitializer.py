import logging
from colorlog import ColoredFormatter
from os import makedirs
from os.path import join, dirname
from settings import LOGGER_CONFIG

formatter = logging.Formatter("%(asctime)s[%(levelname)-8s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
color_formatter = ColoredFormatter(
    "%(white)s%(asctime)s  [%(log_color)s%(levelname)-8s%(reset)s%(white)s] [%(module)-8s:%(lineno)-3d] "
    "%(message)s",
    datefmt="%H:%M:%S",
    reset=True,
    log_colors={
        'DEBUG': 'bold_cyan',
        'INFO': 'bold_green',
        'WARNING': 'bold_yellow',
        'ERROR': 'bold_red',
        'CRITICAL': 'bold_red',
    })

MAIN_DIR = join(dirname(__file__), '..')
LOG_DIR = join(MAIN_DIR, 'log')
# /app/logs
makedirs(LOG_DIR, exist_ok=True)


def initialize_logger(file_output=True):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    level = getattr(logging, LOGGER_CONFIG['CONSOLE_LOG_LEVEL'], 'INFO')
    # create console handler
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(color_formatter)
    logger.addHandler(handler)

    if file_output:
        print(LOGGER_CONFIG['APPEND_LOGS'])
        if LOGGER_CONFIG['APPEND_LOGS']:
            write_flag = "a"
        else:
            write_flag = "w"
        # create error file handler
        handler = logging.FileHandler(join(LOG_DIR, "error.log"), write_flag, encoding=None, delay=True)
        handler.setLevel(logging.ERROR)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # create debug file handler
        handler = logging.FileHandler(join(LOG_DIR, "all.log"), write_flag)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)


initialize_logger()
