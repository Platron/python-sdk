from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException

class MakeRecurringBuilder(RequestBuilder):
    '''
    Make recurring API request
    '''

    def __init__(self, recurring_profile, description):
        """
        Args:
            recurring_profile (string): recurring profile id
            description (string): payment description
        """
        self.pg_recurring_profile = recurring_profile
        self.pg_description = description
        
    def get_url(self):
        return self.PLATRON_URL + 'make_recurring_payment.php'
    
    def add_order_id(self, order):
        """Add order id to recurring transaction
        Args:
            order (string): merchant order id
        Returns:
            self
        """
        self.pg_order_id = order
        return self
    
    def add_amount(self, amount):
        """Add amount to recurring transaction
        Args:
            amount (string): default - amount like in start transaction
        Returns:
            self
        """
        self.pg_amount = amount
        return self
    
    def add_result_url(self, result_url):
        """Add result url to recurring transaction
        Args:
            result_url (string): default - amount like in start transaction
        Returns:
            self
        """
        self.pg_result_url = result_url
        return self
    
    def add_refund_url(self, refund_url):
        """Add refund url to recurring transaction
        Args:
            refund_url (string): default - amount like in start transaction
        Returns:
            self
        """
        self.pg_refund_url = refund_url
        return self
    
    def add_request_method(self, request_method):
        """Add request method to recurring transaction
        Args:
            request_method (string): default - amount like in start transaction
        Returns:
            self
        """
        self.pg_request_method = request_method
        return self
    
    def add_encoding(self, encoding):
        """Add encoding to recurring transaction
        Args:
            encoding (string): default - amount like in start transaction
        Returns:
            self
        """
        self.pg_encoding = encoding
        return self
    
    def add_merchant_params(self, params):
        """Add merchant params to recurring transaction
        Args:
            params (dict): merchant additional params without pg_ names which will get on result
        Returns:
            self
        """
        for param_name in params.keys():
            if param_name.find('pg_') != -1:
                raise  SdkException('Only params without pg_')
            
            setattr(self, param_name, params.get(param_name))
        
        return self    
        