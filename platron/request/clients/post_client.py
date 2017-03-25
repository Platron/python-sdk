import requests
import random

from platron.request.clients.platron_client import PlatronClient
from platron.sig_helper import SigHelper
from platron.sdk_exception import SdkException
import xml.etree.ElementTree

class PostClient(PlatronClient):
    '''
    Send request to platron by post
    '''


    def __init__(self, merchant, secret_key):
        self.merchant = merchant
        self.secret_key = secret_key
    
    def request(self, request_builder):
        try :
            params_to_request = request_builder.get_params()
            params_to_request.update({'pg_merchant_id' : self.merchant})
            params_to_request.update({'pg_salt' : random.randint(1, 10000)})
            
            sig_helper = SigHelper(self.secret_key)
            
            parsed_list = request_builder.get_url().split('/');
            script_name = parsed_list.__getitem__(parsed_list.__len__() - 1)
            
            params_to_request.update({'pg_sig' : sig_helper.make(script_name, params_to_request)})

            response = requests.get(request_builder.get_url(), params_to_request)              
            root = xml.etree.ElementTree.fromstring(response.text)
        except Exception:
            raise SdkException('Cant send request')
        
        for child in root:
            if child.tag == 'pg_error_description':
                pg_error_description = child.text
            if child.tag == 'pg_error_code':
                pg_error_code = child.text
                
        if 'pg_error_code' in locals():
            raise SdkException('Error in response ' + pg_error_description + ' code ' + pg_error_code)
        
        return response.text