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
        
        self.assertEquals('2017-01-01', parameters.get('pg_tripleg_1_date'))
        self.assertEquals('SU', parameters.get('pg_tripleg_1_carrier'))
        self.assertEquals('E', parameters.get('pg_tripleg_1_class'))
        self.assertEquals('KRR', parameters.get('pg_tripleg_1_destination_from'))
        self.assertEquals('VKO', parameters.get('pg_tripleg_1_destination_to'))
        self.assertEquals('X', parameters.get('pg_tripleg_1_stopover'))
        self.assertEquals('NVOR', parameters.get('pg_tripleg_1_fare_basis_code'))
        self.assertEquals('6062', parameters.get('pg_tripleg_1_flight_number'))
        
        with self.assertRaises(SdkException):
            data_object = TripLeg('5', '2017-01-01', 'SU', 'E', 'KRR', 'VKO', 'X', 'NVOR', '6062')