import logging

def setup_logging():
    logging.basicConfig(filename='error.log', level=logging.ERROR)
