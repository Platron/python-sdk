import unittest
from platron.request.request_builders.get_moneyback_status_builder import GetMoneybackStatusBuilder

class GetMoneybackStatusBuiderTest(unittest.TestCase):
    '''
    Get moneyback status builder test
    '''

    def test_get_params(self):
        builder = GetMoneybackStatusBuilder('3344')
        parameters = builder.get_params()
        
        self.assertEqual('3344', parameters.get('pg_moneyback_id'))     