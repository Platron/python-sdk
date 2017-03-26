from platron.request.request_builders.request_builder import RequestBuilder

class GetRegistryBuilder(RequestBuilder):
    '''
    Get status api request builder
    '''
    
    def __init__(self, date):
        """
        Args:
            date (string): date
        """
        self.pg_date = date

    def get_url(self):
        return self.PLATRON_URL + 'get_registry.php'