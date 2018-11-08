from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException


class MakeRecurringBuilder(RequestBuilder):

    def __init__(self, recurring_profile, description):
        """
        :param recurring_profile: digital recurring profile id (string)
        :param description: payment description (string)
        """
        self.pg_recurring_profile = recurring_profile
        self.pg_description = description

    def get_url(self):
        return self.PLATRON_URL + 'make_recurring_payment.php'

    def add_order_id(self, order):
        """
        :param order:  merchant order id (string)
        """
        self.pg_order_id = order

    def add_amount(self, amount):
        """
        :param amount: default - amount like in start transaction (string)
        """
        self.pg_amount = amount

    def add_result_url(self, result_url):
        """
        :param result_url: url to send result (string)
        """
        self.pg_result_url = result_url

    def add_refund_url(self, refund_url):
        """
        :param refund_url: url to send refund result (string)
        """
        self.pg_refund_url = refund_url

    def add_request_method(self, request_method):
        """
        :param request_method: method to send results to merchant GET|POST|XML (string)
        """
        self.pg_request_method = request_method
        return self

    def add_encoding(self, encoding):
        """
        :param encoding: default - amount like in start transaction (string)
        """
        self.pg_encoding = encoding

    def add_merchant_params(self, params):
        """
        :param params: merchant additional params without pg_ names which will get on result (dict)
        """
        for param_name in params.keys():
            if param_name.find('pg_') != -1:
                raise SdkException('Only params without pg_')

            setattr(self, param_name, params.get(param_name))
