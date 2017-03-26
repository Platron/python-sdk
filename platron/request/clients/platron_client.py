import abc

class PlatronClient(metaclass=abc.ABCMeta):
    '''
    Base client class
    '''

    @abc.abstractmethod
    def __init__(self, merchant, secret_key):
        pass
    
    @abc.abstractmethod
    def request(self, url, params):
        pass      