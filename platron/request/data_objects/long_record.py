from platron.request.data_objects.data_object import DataObject
from platron.request.data_objects.tripleg import TripLeg
from platron.sdk_exception import SdkException


class LongRecord(DataObject):

    def __init__(self, passenger_name, ticket_number, ticket_restricted):
        """
        Args:
            :param passenger_name: passenger name (string)
            :param ticket_number: ticket number (string)
            :param ticket_restricted: restricted ticket or not (1|0) (string)
        """
        self.pg_ticket_passenger_name = passenger_name
        self.pg_ticket_number = ticket_number
        self.pg_ticket_restricted = ticket_restricted

    def set_ticket_system(self, ticket_system):
        """
        :param ticket_system: ticket system (string)
        """
        self.pg_ticket_system = ticket_system

    def set_agency_code(self, agency_code):
        """
        :param agency_code: agency code (string)
        """
        self.pg_ticket_agency_code = agency_code

    def add_tripleg(self, tripleg):
        """
        :param tripleg: One of four triplegs (TripLeg)
        """
        if not isinstance(tripleg, TripLeg):
            raise SdkException('Only long record object expected')

        params = tripleg.get_params()
        for param_name in params.keys():
            setattr(self, param_name, params.get(param_name))
