import unittest
from platron.request.data_objects.avia_gds import AviaGds

class AviaGdsTest(unittest.TestCase):
    '''
    AviaGds data object test
    '''

    def test_get_parameters(self):
        data_object = AviaGds('GGG666', 'SABRE', '10.00')
        data_object.add_card_brands({'1' : 'VI', '2' : 'CA'})
        
        params = data_object.get_params()
        
        self.assertEqual('GGG666', params.get('pg_rec_log'))
        self.assertEqual('SABRE', params.get('pg_gds'))
        self.assertEqual('10.00', params.get('pg_merchant_markup'))
        self.assertEqual('VI', params.get('pg_card_brand').get('1'))
        self.assertEqual('CA', params.get('pg_card_brand').get('2'))