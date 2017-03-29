import unittest
from platron.request.request_builders.ps_list_builder import PsListBuilder

class PsListBuiderTest(unittest.TestCase):
    '''
    Ps list builder test
    '''

    def test_get_params(self):
        builder = PsListBuilder('10.00')
        builder.add_currency('RUB')
        builder.add_testing_mode()
        
        parameters = builder.get_params()
        
        self.assertEqual('10.00', parameters.get('pg_amount'))
        self.assertEqual('RUB', parameters.get('pg_currency'))
        self.assertEqual(1, parameters.get('pg_testing_mode'))