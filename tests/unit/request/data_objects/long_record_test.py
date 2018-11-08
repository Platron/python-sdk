import unittest
from platron.request.data_objects.long_record import LongRecord
from platron.request.data_objects.tripleg import TripLeg
from unittest.mock import Mock
from unittest.mock import MagicMock


class LongRecordTest(unittest.TestCase):

    def test_get_parameters(self):
        data_object = LongRecord('alexey lashnev', 'FFF666', '1')
        data_object.set_agency_code('F')
        data_object.set_ticket_system('GAT')

        triplegStub = Mock(spec=TripLeg)
        triplegStub.get_params = MagicMock(return_value={'long_record_test': 'long_record_test'})

        data_object.add_tripleg(triplegStub)

        params = data_object.get_params()

        self.assertEqual('alexey lashnev', params.get('pg_ticket_passenger_name'))
        self.assertEqual('FFF666', params.get('pg_ticket_number'))
        self.assertEqual('1', params.get('pg_ticket_restricted'))
        self.assertEqual('F', params.get('pg_ticket_agency_code'))
        self.assertEqual('GAT', params.get('pg_ticket_system'));
        self.assertEqual('long_record_test', params.get('long_record_test'));
