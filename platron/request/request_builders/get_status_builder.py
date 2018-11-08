from platron.request.request_builders.request_builder import RequestBuilder


class GetStatusBuilder(RequestBuilder):

    def __init__(self, payment=None, order=None):
        """
        :param payment: digital platron payment id (string)
        :param order: merchant order id (string)
        """
        if payment == None:
            self.pg_order_id = order
        else:
            self.pg_payment_id = payment

    def get_url(self):
        return self.PLATRON_URL + 'get_status.php'
