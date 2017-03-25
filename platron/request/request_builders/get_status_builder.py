from platron.request.request_builders.request_builder import RequestBuilder

class GetStatusBuilder(RequestBuilder):
    '''
    Get status API request
    '''

    def __init__(self, payment = None, order = None):
        if payment == None:
            self.pg_order_id = order
        else:
            self.pg_payment_id = payment
            
    def get_url(self):
        return self.PLATRON_URL + 'get_status.php'