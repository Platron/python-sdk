from platron.request.request_builders.request_builder import RequestBuilder

class CancelBuilder(RequestBuilder):
    '''
    Cancel api request
    '''

    def __init__(self, payment):
        self.pg_payment_id = payment
        
    def get_url(self):
        return self.PLATRON_URL + 'cancel.php'     