from platron.request.request_builders.request_builder import RequestBuilder


class CreateRefundRequestBuider(RequestBuilder):

    def __init__(self, payment, amount, comment):
        """
        :param payment: digital platron payment id (string)
        :param amount: amount to refund request (string)
        :param comment: reason of refund (string)
        """
        self.pg_payment_id = payment
        self.pg_refund_amount = amount
        self.pg_comment = comment

    def get_url(self):
        return self.PLATRON_URL + 'create_refund_request.php'
