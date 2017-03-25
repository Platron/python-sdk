from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException
from platron.request.data_objects.long_record import BankCard
from platron.request.data_objects.avia_gds import AviaGds

class InitPaymentBuilder(RequestBuilder):
    '''
    Init payment API request
    '''

    def __init__(self, amount, description):
        self.pg_amount = amount
        self.pg_description = description
        
    def get_url(self):
        return self.PLATRON_URL + 'init_payment.php'
    
    def add_bankcard(self, bankcard):
        if type(bankcard) != BankCard:
            raise SdkException('Only long record object expected')
        
        bank_card_params = bankcard.get_params()
        for param_name in bank_card_params.keys():
            setattr(self, param_name, bank_card_params.get(param_name))
            
        return self
    
    def add_gds(self, avia_gds):
        if type(avia_gds) != AviaGds:
            raise SdkException('Only long record object expected')
        
        avia_gds_params = avia_gds.get_params()
        for param_name in avia_gds_params.keys():
            setattr(self, param_name, avia_gds_params.get(param_name))
            
        return self
    
    def add_payment_system(self, payment_system):
        self.pg_payment_system = payment_system
        return self
    
    def add_order_id(self, order_id):
        self.pg_order_id = order_id
        return self
    
    def add_currency(self, currency):
        self.pg_currency = currency
        return self
    
    def add_lifetime(self, lifetime):
        self.pg_lifetime = lifetime
        return self
    
    def add_postpone(self):
        self.pg_postpone = 1
        return self
    
    def add_language_en(self):
        self.pg_language = 'en'
        return self
    
    def add_testing_mode(self):
        self.pg_testing_mode = 1
        return self
    
    def add_recurring_start(self):
        self.pg_recurring_start = 1
        return self
    
    def add_check_url(self, url):
        self.pg_check_url = url
        return self
    
    def add_result_url(self, url):
        self.pg_result_url = url
        return self
    
    def refund_url(self, url):
        self.pg_refund_url = url
        return self
    
    def add_capture_url(self, url):
        self.pg_capture_url = url
        return self
    
    def add_request_method(self, method):
        self.pg_request_method = method
        return self
    
    def add_success_url(self, url):
        self.pg_success_url = url
        return self
    
    def add_success_url_method(self, method):
        self.pg_success_url_method = method
        return self
    
    def add_state_url(self, url):
        self.pg_state_url = url
        return self
    
    def add_state_url_method(self, method):
        self.pg_state_url_method = method
        return self
    
    def add_failure_url(self, url):
        self.pg_failure_url = url
        return self
    
    def add_failure_url_method(self, method):
        self.pg_failure_url_method = method
        return self
    
    def add_site_url(self, url):
        self.pg_site_url = url
        return self
    
    def add_user_phone(self, user_phone):
        self.pg_user_phone = user_phone
        return self
    
    def add_user_email(self, user_email):
        self.pg_user_email = user_email
        return self
    
    def add_user_ip(self, user_ip):
        self.pg_user_ip = user_ip
        return self
    
    def add_merchant_params(self, params):
        for param_name in params.keys():
            if param_name.find('pg_'):
                raise  SdkException('Only params without pg_')
            
            setattr(self, param_name, params.get(param_name))
        
        return self   