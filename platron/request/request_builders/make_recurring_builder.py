from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException

class MakeRecurringBuilder(RequestBuilder):
    '''
    Make recurring API request
    '''

    def __init__(self, recurring_profile, description):
        self.pg_recurring_profile = recurring_profile
        self.pg_description = description
        
    def get_url(self):
        return self.PLATRON_URL + 'make_recurring_payment.php'
    
    def add_order_id(self, order):
        self.pg_order_id = order
        return self
    
    def add_amount(self, amount):
        self.pg_amount = amount
        return self
    
    def add_result_url(self, result_url):
        self.pg_result_url = result_url
        return self
    
    def add_refund_url(self, refund_url):
        self.pg_refund_url = refund_url
        return self
    
    def add_request_method(self, request_method):
        self.pg_request_method = request_method
        return self
    
    def add_encoding(self, encoding):
        self.pg_encoding = encoding
        return self
    
    def add_merchant_params(self, params):
        for param_name in params.keys():
            if param_name.find('pg_'):
                raise  SdkException('Only params without pg_')
            
            setattr(self, param_name, params.get(param_name))
        
        return self    
        