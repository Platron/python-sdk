from platron.request.request_builders.request_builder import RequestBuilder


class CancelBuilder(RequestBuilder):

    def __init__(self, payment):
        """
        :param payment: digital platron payment id (string)
        """
        self.pg_payment_id = payment

    def get_url(self):
        return self.PLATRON_URL + 'cancel.php'
