import unittest
from unittest.mock import patch
from platron.request.data_objects.long_record import LongRecord
from platron.request.data_objects.tripleg import TripLeg

class LongRecordTest(unittest.TestCase):
    '''
    LongRecord data object test
    '''

    @patch("platron.request.data_objects.tripleg.TripLeg.__init__")
    def test_get_parameters(self, mock_tripleg):      
        data_object = LongRecord('alexey lashnev', 'FFF666', '1')
        data_object.set_agency_code('F')
        data_object.set_ticket_system('GAT')
      
        params = data_object.get_params()
        
        self.assertEquals('alexey lashnev', params.get('pg_ticket_passenger_name'))
        self.assertEquals('FFF666', params.get('pg_ticket_number'))
        self.assertEquals('1', params.get('pg_ticket_restricted'))
        self.assertEquals('F', params.get('pg_ticket_agency_code'))
        self.assertEquals('GAT', params.get('pg_ticket_system'));