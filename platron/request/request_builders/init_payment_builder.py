from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException
from platron.request.data_objects.bank_card import BankCard
from platron.request.data_objects.avia_gds import AviaGds

class InitPaymentBuilder(RequestBuilder):
    '''
    Init payment API request
    '''

    def __init__(self, amount, description):
        """
        Args:
            amount (string): payment amount
            description (string): payment description
        """
        self.sdk = 'pythonsdk'
        self.pg_amount = amount
        self.pg_description = description
        
    def get_url(self):
        return self.PLATRON_URL + 'init_payment.php'
    
    def add_bankcard(self, bankcard):
        """Add bankcard to request
        Args:
            bankcard (BankCard): bank card data
        Returns:
            self
        """
        if not isinstance(bankcard, BankCard):
            raise SdkException('Only long record object expected')
        
        bank_card_params = bankcard.get_params()
        for param_name in bank_card_params.keys():
            setattr(self, param_name, bank_card_params.get(param_name))
            
        return self
    
    def add_gds(self, avia_gds):
        """Add gds to request
        Args:
            avia_gds (AviaGds): avia gds data
        Returns:
            self
        """
        if not isinstance(avia_gds, AviaGds):
            raise SdkException('Only long record object expected')
        
        avia_gds_params = avia_gds.get_params()
        for param_name in avia_gds_params.keys():
            setattr(self, param_name, avia_gds_params.get(param_name))
            
        return self
    
    def add_payment_system(self, payment_system):
        """Add payment system to request
        Args:
            payment_system (string): payment system
        Returns:
            self
        """
        self.pg_payment_system = payment_system
        return self
    
    def add_order_id(self, order_id):
        """Add order id to request
        Args:
            order_id (string): merchant order id
        Returns:
            self
        """
        self.pg_order_id = order_id
        return self
    
    def add_currency(self, currency):
        """Add currency to request
        Args:
            currency (string): currency. default RUB 
        Returns:
            self
        """
        self.pg_currency = currency
        return self
    
    def add_lifetime(self, lifetime):
        """Add lifetime to request
        Args:
            lifetime (string): Time in seconds. Default 7 day. Min 2 hour, max 7 days
        Returns:
            self
        """
        self.pg_lifetime = lifetime
        return self
    
    def add_postpone(self):
        """Set transaction postponed
        Returns:
            self
        """
        self.pg_postpone = 1
        return self
    
    def add_language_en(self):
        """Set transaction language en
        Returns:
            self
        """
        self.pg_language = 'en'
        return self
    
    def add_testing_mode(self):
        """Set transaction in test mode
        Returns:
            self
        """
        self.pg_testing_mode = 1
        return self
    
    def add_recurring_start(self):
        """Start recurring transaction
        Returns:
            self
        """
        self.pg_recurring_start = 1
        return self
    
    def add_check_url(self, url):
        """Add check url to transaction
        Args:
            url (string): Check url
        Returns:
            self
        """
        self.pg_check_url = url
        return self
    
    def add_result_url(self, url):
        """Add result url to transaction
        Args:
            url (string): Result url
        Returns:
            self
        """
        self.pg_result_url = url
        return self
    
    def add_refund_url(self, url):
        """Add refund url to transaction
        Args:
            url (string): Refund url
        Returns:
            self
        """
        self.pg_refund_url = url
        return self
    
    def add_capture_url(self, url):
        """Add capture url to transaction
        Args:
            url (string): Capture url
        Returns:
            self
        """
        self.pg_capture_url = url
        return self
    
    def add_request_method(self, method):
        """Add reuqst method to transaction
        Args:
            method (string): method which will be used to request merchant
        Returns:
            self
        """
        self.pg_request_method = method
        return self
    
    def add_success_url(self, url):
        """Add success url to transaction
        Args:
            url (string): success url
        Returns:
            self
        """
        self.pg_success_url = url
        return self
    
    def add_success_url_method(self, method):
        """Add success url method to transaction
        Args:
            method (string): method which will be used when send user on success url
        Returns:
            self
        """
        self.pg_success_url_method = method
        return self
    
    def add_state_url(self, url):
        """Add state url to transaction
        Args:
            url (string): state url
        Returns:
            self
        """
        self.pg_state_url = url
        return self
    
    def add_state_url_method(self, method):
        """Add state url method to transaction
        Args:
            method (string): method which will be used when send user on state url
        Returns:
            self
        """
        self.pg_state_url_method = method
        return self
    
    def add_failure_url(self, url):
        """Add failure url to transaction
        Args:
            url (string): failure url
        Returns:
            self
        """
        self.pg_failure_url = url
        return self
    
    def add_failure_url_method(self, method):
        """Add failure url method to transaction
        Args:
            method (string): method which will be used when send user on failure url
        Returns:
            self
        """
        self.pg_failure_url_method = method
        return self
    
    def add_site_url(self, url):
        """Add site url to transaction
        Args:
            url (string): site url
        Returns:
            self
        """
        self.pg_site_url = url
        return self
    
    def add_user_phone(self, user_phone):
        """Add user phone to transaction
        Args:
            user_phone (string): digital user phone like 79095555555
        Returns:
            self
        """
        self.pg_user_phone = user_phone
        return self
    
    def add_user_email(self, user_email):
        """Add user email to transaction
        Args:
            user_email (string): user email
        Returns:
            self
        """
        self.pg_user_contact_email = user_email
        return self
    
    def add_user_ip(self, user_ip):
        """Add user ip to transaction
        Args:
            user_ip (string): real user ip
        Returns:
            self
        """
        self.pg_user_ip = user_ip
        return self
    
    def add_merchant_params(self, params):
        """Add merchant params
        Args:
            params (dict): merchant params without pg_ names which will get on result
        Returns:
            self
        """
        for param_name in params.keys():
            if param_name.find('pg_') != -1:
                raise  SdkException('Only params without pg_')
            
            setattr(self, param_name, params.get(param_name))
        
        return self
    
    def add_ps_additional_parameters(self, params):
        """Add ps additional params
        Args:
            params (dict): ps additional params with pg_ names
        Returns:
            self
        """
        for param_name in params.keys():
            if param_name.find('pg_') == -1:
                raise  SdkException('Only params without pg_')
            
            setattr(self, param_name, params.get(param_name))
        
        return self   