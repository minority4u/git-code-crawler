import logging
import os
import App.Settings as Const


# Define individual logger at one point to reuse it in all modules

class Console_and_file_logger():
    def __init__(self, logfile_name='Trimming_Log'):
        """
        Create your own logger
        prints all messages into the given logfile and ouput it on console
        :param logfile_name:
        """

        # Define the general formatting schema
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        logger = logging.getLogger()


        # Create log directory
        log_dir = os.getcwd() + Const.DIR_TO_LOGFILE
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Define logfile handler and file
        hdlr = logging.FileHandler(log_dir + logfile_name + '.log')
        hdlr.setFormatter(formatter)

        # Define console output handler
        hdlr_console = logging.StreamHandler()
        hdlr_console.setFormatter(formatter)

        # Add both handlers to our logger instance
        logger.addHandler(hdlr)
        logger.addHandler(hdlr_console)
        logger.setLevel(logging.INFO)

        print('Log dir: ' + log_dir)
        logging.info('Starts ' + logfile_name)


if __name__ == "__main__":
    logger = Console_and_file_logger(os.path.basename(__file__))
