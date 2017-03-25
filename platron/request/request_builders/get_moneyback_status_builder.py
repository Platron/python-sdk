from platron.request.request_builders.request_builder import RequestBuilder

class GetMoneybackStatusBuilder(RequestBuilder):
    '''
    Get moneyback status API request
    '''


    def __init__(self, moneyback):
        self.pg_moneyback_id = moneyback
        
    def get_url(self):
        return self.PLATRON_URL + 'get_moneyback_status.php'