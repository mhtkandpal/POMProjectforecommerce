import logging


class LogGen:
    @staticmethod
    def loggen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename='/home/arcgate/PycharmProjects/POMProjectforecommerce/Logs/automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger


##logging.basicConfig(filename='\home\arcgate\PycharmProjects\POMProjectforecommerce\Logs\automation.log',
       #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #logger = logging.getLogger()
        #logger.setLevel(logging.INFO)
        #return logger
