import logging

logging.basicConfig()

class ObjectsFactory:
    @staticmethod
    def getLogger(loggerName):
        logRet = logging.getLogger(loggerName)
        return logRet