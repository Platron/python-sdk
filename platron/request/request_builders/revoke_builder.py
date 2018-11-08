from platron.request.request_builders.request_builder import RequestBuilder


class RevokeBuilder(RequestBuilder):

    def __init__(self, payment):
        """
        :param payment: digital platron payment id (string)
        """
        self.pg_payment_id = payment

    def get_url(self):
        return self.PLATRON_URL + 'revoke.php'

    def set_amount(self, amount):
        """
        :param amount: default - full amount (string)
        """
        self.pg_refund_amount = amount
