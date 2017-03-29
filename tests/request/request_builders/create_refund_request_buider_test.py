import unittest
from platron.request.request_builders.create_refund_request_builder import CreateRefundRequestBuider

class CreateRefundRequestBuiderTest(unittest.TestCase):
    '''
    Create refund request buider test
    '''

    def test_get_params(self):
        builder = CreateRefundRequestBuider('34324324', '10.00', 'test')
        params = builder.get_params()
        
        self.assertEqual('34324324', params.get('pg_payment_id'))
        self.assertEqual('10.00', params.get('pg_refund_amount'))
        self.assertEqual('test', params.get('pg_comment'))
        