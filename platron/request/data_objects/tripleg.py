from platron.request.data_objects.data_object import DataObject
from platron.sdk_exception import SdkException

class TripLeg(DataObject):
    '''
    Tripleg data to set in long record
    '''

    def __init__(self, tripleg_number, date, carrier, class_transport, dest_from, dest_to, stop_over, basis_code, flight_number):
        """
        Args:
            tripleg_number (string): flight number
            date (string): date of tripleg
            carrier (string): carrier code
            class_transport (string): transport class
            dest_from (string): aiport from code
            dest_to (string): aiport to code
            stop_over (string): can stop (O|X)
            basis_code (string): tariff code
            flight_number (string): fligth number
        """       
        if int(tripleg_number) <= 0 or int(tripleg_number) > 4:
            raise SdkException('Only 4 tripleg could be send')
            
        setattr(self, 'pg_tripleg_' + tripleg_number + '_date', date)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_carrier', carrier)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_class', class_transport)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_destination_from', dest_from)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_destination_to', dest_to)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_stopover', stop_over)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_fare_basis_code', basis_code)
        setattr(self, 'pg_tripleg_' + tripleg_number + '_flight_number', flight_number)