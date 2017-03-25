from platron.request.request_builders.request_builder import RequestBuilder

class PsListBuilder(RequestBuilder):
    '''
    Ps list API requests
    '''

    def __init__(self, amount):
        self.pg_amount = amount
        
    def get_url(self):
        return self.PLATRON_URL + 'ps_list.php'
    
    def add_currency(self, currency):
        self.pg_currency = currency
        return self
    
    def add_testing_mode(self):
        self.pg_testing_mode = 1
        return self