import logging

logger = logging.getLogger('sample_example')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
file_hand = logging.FileHandler('spam.log')
file_hand.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
file_hand.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(file_hand)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
