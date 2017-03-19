import abc

class RequestBuilder(metaclass=abc.ABCMeta):
    '''
    Base builder class
    '''
    
    PLATRON_URL = 'https://www.platron.ru/'

    def get_url(self):
        pass
    
    def get_params(self):
        return {}