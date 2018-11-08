from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException
from platron.request.data_objects.bank_card import BankCard
from platron.request.data_objects.avia_gds import AviaGds


class InitPaymentBuilder(RequestBuilder):

    def __init__(self, amount, description):
        """
        :param amount: payment amount (string)
        :param description: payment description (string)
        """
        self.sdk = 'pythonsdk'
        self.pg_amount = amount
        self.pg_description = description

    def get_url(self):
        return self.PLATRON_URL + 'init_payment.php'

    def add_bankcard(self, bankcard):
        """
        :param bankcard: bank card data (BankCard)
        """
        if not isinstance(bankcard, BankCard):
            raise SdkException('Only long record object expected')

        bank_card_params = bankcard.get_params()
        for param_name in bank_card_params.keys():
            setattr(self, param_name, bank_card_params.get(param_name))

    def add_gds(self, avia_gds):
        """
        :param avia_gds: avia gds data (AviaGds)
        """
        if not isinstance(avia_gds, AviaGds):
            raise SdkException('Only long record object expected')

        avia_gds_params = avia_gds.get_params()
        for param_name in avia_gds_params.keys():
            setattr(self, param_name, avia_gds_params.get(param_name))

    def add_payment_system(self, payment_system):
        """
        :param payment_system: payment system chosen customer (string)
        """
        self.pg_payment_system = payment_system

    def add_order_id(self, order_id):
        """
        :param order_id: merchant order id (string)
        """
        self.pg_order_id = order_id

    def add_currency(self, currency):
        """
        :param currency: currency. default RUB (string)
        """
        self.pg_currency = currency

    def add_lifetime(self, lifetime):
        """
        :param lifetime: Time in seconds. Default 7 day. Min 2 hour, max 7 days (int)
        """
        self.pg_lifetime = lifetime

    def add_postpone(self):
        self.pg_postpone = 1

    def add_language_en(self):
        self.pg_language = 'en'

    def add_testing_mode(self):
        self.pg_testing_mode = 1

    def add_recurring_start(self):
        self.pg_recurring_start = 1

    def add_check_url(self, url):
        """
        :param url: check url (string)
        """
        self.pg_check_url = url

    def add_result_url(self, url):
        """
        :param url: result url (string)
        """
        self.pg_result_url = url

    def add_refund_url(self, url):
        """
        :param url: refund url (string)
        """
        self.pg_refund_url = url
        return self

    def add_capture_url(self, url):
        """
        :param url: capture url (string)
        """
        self.pg_capture_url = url
        return self

    def add_request_method(self, method):
        """
        :param method: method which will be used to request merchant (string)
        """
        if self.__get_request_method_variables().get(method) == None:
            raise SdkException('Wrong request method. Use from constants')

        self.pg_request_method = method

    def add_success_url(self, url):
        """
        :param url: success url to send customer (string)
        """
        self.pg_success_url = url

    def add_success_url_method(self, method):
        """
        :param method: method which will be used when send user on success url (string)
        """
        if self.__get_redirect_method_variables().get(method) == None:
            raise SdkException('Wrong method. Use from constants')

        self.pg_success_url_method = method

    def add_state_url(self, url):
        """
        :param url: state url where customer need to wait (string)
        """
        self.pg_state_url = url

    def add_state_url_method(self, method):
        """
        :param method: method which will be used when send user on state url (string)
        """
        if self.__get_redirect_method_variables().get(method) == None:
            raise SdkException('Wrong method. Use from constants')

        self.pg_state_url_method = method

    def add_failure_url(self, url):
        """
        :param url: failure url to send customer (string)
        """
        self.pg_failure_url = url

    def add_failure_url_method(self, method):
        """
        :param method: method which will be used when send user on failure url (string)
        """
        if self.__get_redirect_method_variables().get(method) == None:
            raise SdkException('Wrong method. Use from constants')

        self.pg_failure_url_method = method

    def add_site_url(self, url):
        """
        :param url: site url to show to customer (string)
        """
        self.pg_site_url = url

    def add_user_phone(self, user_phone):
        """
        :param user_phone: digital user phone like 79095555555 (string)
        """
        self.pg_user_phone = user_phone

    def add_user_email(self, user_email):
        """
        :param user_email: user email (string)
        """
        self.pg_user_contact_email = user_email
        return self

    def add_user_ip(self, user_ip):
        """
        :param user_ip: real user ip v4 - not local (string)
        """
        self.pg_user_ip = user_ip

    def add_merchant_params(self, params):
        """
        :param params: merchant params without pg_ names which will get on result (Dict)
        """
        for param_name in params.keys():
            if param_name.find('pg_') != -1:
                raise SdkException('Only params without pg_')

            setattr(self, param_name, params.get(param_name))

    def add_ps_additional_parameters(self, params):
        """
        :param params: ps additional params with pg_ names (Dict)
        """
        for param_name in params.keys():
            if param_name.find('pg_') == -1:
                raise SdkException('Only params without pg_')

            setattr(self, param_name, params.get(param_name))

    @staticmethod
    def __get_request_method_variables():
        return {'GET': True, 'POST': True, 'XML': True}

    @staticmethod
    def __get_redirect_method_variables():
        return {'GET': True, 'POST': True, 'AUTOGET': True, 'AUTOPOST': True}
