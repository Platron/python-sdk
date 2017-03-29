import unittest
from platron.request.request_builders.get_registry_builder import GetRegistryBuilder

class GetRegistryBuiderTest(unittest.TestCase):
    '''
    Get registry buider test
    '''

    def test_get_params(self):
        builder = GetRegistryBuilder('2016-01-01')
        params = builder.get_params()
        
        self.assertEqual('2016-01-01', params.get('pg_date'))