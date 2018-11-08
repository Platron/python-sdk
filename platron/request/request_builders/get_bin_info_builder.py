from platron.request.request_builders.request_builder import RequestBuilder


class GetBinInfoBuilder(RequestBuilder):

    def __init__(self, card_bin):
        """
        :param card_bin: first 6 characters of card number (string)
        """
        self.pg_bin = card_bin

    def get_url(self):
        return self.PLATRON_URL + 'get_bin_info.php'
