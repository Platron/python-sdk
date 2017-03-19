import abc

class Client(metaclass=abc.ABCMeta):
    '''
    Base client class
    '''

    @abc.abstractmethod
    def __init__(self, merchant, secret_key):
        pass
    
    def request(self, url, params):
        pass      