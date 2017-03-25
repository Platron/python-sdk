from platron.request.request_builders.request_builder import RequestBuilder

class RevokeBuilder(RequestBuilder):
    '''
    Revoke API request
    '''

    def __init__(self, payment):
        self.pg_payment_id = payment
    
    def set_amount(self, amount):
        self.pg_refund_amount = amount