from platron.request.data_objects.data_object import DataObject
from platron.request.data_objects.tripleg import TripLeg
from platron.sdk_exception import SdkException

class LongRecord(DataObject):
    '''
    Long record data to send in DoCapture request
    '''

    def __init__(self, passanger_name, ticket_number, ticket_restricked):
        """
        Args:
            passanger_name (string): passanger name
            ticket_number (string): ticket number
            ticket_restricked (string): restricted ticket or not (1|0)
        """
        self.pg_ticket_passenger_name = passanger_name
        self.pg_ticket_number = ticket_number
        self.pg_ticket_restricted = ticket_restricked
        
    def set_ticket_system(self, ticket_system):
        """Add ticket system
        Args:
            ticket_system (string): ticket system
        Returns:
            self
        """
        self.pg_ticket_system = ticket_system
        return self
    
    def set_agency_code(self, agency_code):
        """Add agency code
        Args:
            agency_code (string): agency code
        Returns:
            self
        """
        self.pg_ticket_agency_code = agency_code
        return self
    
    def add_tripleg(self, tripleg):
        """Add tripleg
        Args:
            tripleg (TripLeg): One of four triplegs
        Returns:
            self
        """
        if type(tripleg) != TripLeg:
            raise SdkException('Only long record object expected')
        
        for param_name in tripleg.keys():
            setattr(self, param_name, tripleg.get(param_name))
            
        return self