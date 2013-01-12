from abc import ABCMeta
from abc import abstractmethod

class DbManager:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def connect(self, connectionObject):
        pass
    
    @abstractmethod
    def run_query(self, query):
        pass
    