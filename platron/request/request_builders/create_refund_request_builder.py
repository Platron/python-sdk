from platron.request.request_builders.request_builder import RequestBuilder

class CreateRefundRequestBuider(RequestBuilder):
    '''
    Create refund request API 
    '''

    def __init__(self, payment, amount, comment):
        """
        Args:
            payment (string): platron payment id
            amount (string): amount to refund requst
            comment (string): reason of refund
        """
        self.pg_payment_id = payment
        self.pg_refund_amount = amount
        self.pg_comment = comment
    
    def get_url(self):
        return self.PLATRON_URL + 'create_refund_request.php'