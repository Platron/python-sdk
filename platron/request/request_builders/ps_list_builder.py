from platron.request.request_builders.request_builder import RequestBuilder

class PsListBuilder(RequestBuilder):
    '''
    Ps list API requests
    '''

    def __init__(self, amount):
        """
        Args:
            amount (string): payment amount
        """
        self.pg_amount = amount
        
    def get_url(self):
        return self.PLATRON_URL + 'ps_list.php'
    
    def add_currency(self, currency):
        """Add currency in request to get amount from nerchant currency
        Args:
            currency (string): default RUB
        Returns:
            self
        """
        self.pg_currency = currency
        return self
    
    def add_testing_mode(self):
        """Add test mode to get test payment systems
        Returns:
            self
        """
        self.pg_testing_mode = 1
        return self