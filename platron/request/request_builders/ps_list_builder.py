from platron.request.request_builders.request_builder import RequestBuilder


class PsListBuilder(RequestBuilder):

    def __init__(self, amount):
        """
        :param amount: payment amount (string)
        """
        self.pg_amount = amount

    def get_url(self):
        return self.PLATRON_URL + 'ps_list.php'

    def add_currency(self, currency):
        """
        :param currency: default RUB (string)
        """
        self.pg_currency = currency

    def add_testing_mode(self):
        self.pg_testing_mode = 1
