from platron.request.request_builders.request_builder import RequestBuilder


class GetRegistryBuilder(RequestBuilder):

    def __init__(self, date):
        """
        :param date: date of registry (string)
        """
        self.pg_date = date

    def get_url(self):
        return self.PLATRON_URL + 'get_registry.php'
