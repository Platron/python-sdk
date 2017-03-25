from platron.request.request_builders.request_builder import RequestBuilder

class CreateRefundRequest(RequestBuilder):
    '''
    Create refund request API 
    '''

    def __init__(self, payment, amount, comment):
        self.pg_payment_id = payment
        self.pg_refund_amount = amount
        self.pg_comment = comment
    
    def get_url(self):
        return self.PLATRON_URL + 'create_refund_request.php'