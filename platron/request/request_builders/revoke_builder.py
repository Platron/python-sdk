from platron.request.request_builders.request_builder import RequestBuilder

class RevokeBuilder(RequestBuilder):
    '''
    Revoke API request
    '''

    def __init__(self, payment):
        """
        Args:
            payment (string): platron payment id
        """
        self.pg_payment_id = payment
        
    def get_url(self):
        return self.PLATRON_URL + 'revoke.php'
    
    def set_amount(self, amount):
        """Add amount to request
        Args:
            amount (string): default - full amount
        """
        self.pg_refund_amount = amount