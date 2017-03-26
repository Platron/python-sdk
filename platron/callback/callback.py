from platron.sig_helper import SigHelper
from platron.sdk_exception import SdkException

class Callback(object):
    '''
    Callback helper to process request from platron
    '''

    def __init__(self, script_name, secret_key):
        self.script_name = script_name
        self.sig_helper = SigHelper(secret_key)
        
    def __response(self, salt, status, description):
        pass
    
    def validate_sig(self, params):
        try :
            pg_sig = params.get('pg_sig')
        except Exception:
            raise SdkException('No pg_sig in request')    
        
        return self.sig_helper.check(pg_sig, self.script_name, params)
    
    def response_error(self, params, error):
        try :
            pg_salt = params.get('pg_salt')
        except Exception:
            raise SdkException('No pg_salt in request')
        
        return self.__response(pg_salt, 'error', error)
    
    def response_ok(self, params):
        try :
            pg_salt = params.get('pg_salt')
        except Exception:
            raise SdkException('No pg_salt in request')
        
        return self.__response(pg_salt, 'ok', 'ok')
    
    def response_rejected(self, params, description):
        try :
            pg_salt = params.get('pg_salt')
        except Exception:
            raise SdkException('No pg_salt in request')
        
        return self.__response(pg_salt, 'rejected', description)
    
    def can_reject(self, params):
        try :
            can_reject = params.get('pg_can_reject')
        except Exception:
            return 0
        
        return can_reject