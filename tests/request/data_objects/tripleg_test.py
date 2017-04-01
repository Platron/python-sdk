import unittest
from platron.request.data_objects.tripleg import TripLeg
from platron.sdk_exception import SdkException

class TripLegTest(unittest.TestCase):
    '''
    Tripleg data object test
    '''

    def test_get_parameters(self):
        data_object = TripLeg('1', '2017-01-01', 'SU', 'E', 'KRR', 'VKO', 'X', 'NVOR', '6062')
        parameters = data_object.get_params()
        
        self.assertEqual('2017-01-01', parameters.get('pg_tripleg_1_date'))
        self.assertEqual('SU', parameters.get('pg_tripleg_1_carrier'))
        self.assertEqual('E', parameters.get('pg_tripleg_1_class'))
        self.assertEqual('KRR', parameters.get('pg_tripleg_1_destination_from'))
        self.assertEqual('VKO', parameters.get('pg_tripleg_1_destination_to'))
        self.assertEqual('X', parameters.get('pg_tripleg_1_stopover'))
        self.assertEqual('NVOR', parameters.get('pg_tripleg_1_fare_basis_code'))
        self.assertEqual('6062', parameters.get('pg_tripleg_1_flight_number'))
        
        with self.assertRaises(SdkException):
            TripLeg('5', '2017-01-01', 'SU', 'E', 'KRR', 'VKO', 'X', 'NVOR', '6062')