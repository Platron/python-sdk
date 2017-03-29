import unittest
from platron.request.request_builders.cancel_builder import CancelBuilder

class CancelBuilderTest(unittest.TestCase):
    '''
    Cancel builder test
    '''

    def test_get_parameters(self):
        builder = CancelBuilder('363654')
        params = builder.get_params()
        
        self.assertEqual('363654', params.get('pg_payment_id'))        