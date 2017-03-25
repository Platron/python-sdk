import datetime
from platron.request.request_builders.request_builder import RequestBuilder

class GetRegistryBuilder(RequestBuilder):
    '''
    Get status api request builder
    '''

    def get_url(self):
        return self.PLATRON_URL + 'get_status.php'
    
    def get_params(self):
        return {'date' : datetime.date.today()}