import requests
import random

from platron.request.clients.platron_client import PlatronClient
from platron.sig_helper import SigHelper
from platron.sdk_exception import SdkException
from xml.etree.ElementTree import Element, SubElement, tostring, fromstring

class PostClient(PlatronClient):
    '''
    Send request to platron by post
    '''

    def __init__(self, merchant, secret_key):
        """
        Args:
            merchant (string): merchant id from https://www.platron.ru/admin/merchants.php
            secret_key (string): merchant secret key from https://www.platron.ru/admin/merchants.php
        """
        self.merchant = merchant
        self.secret_key = secret_key
    
    def request(self, request_builder):
        """Send post request and check errors
        Args:
            request_builder (RequestBuilder): instance of RequestBuilder
        Returns:
            String
        """
        try :
            params_to_request = request_builder.get_params()
            params_to_request.update({'pg_merchant_id' : self.merchant})
            params_to_request.update({'pg_salt' : random.randint(1, 10000)})
            
            sig_helper = SigHelper(self.secret_key)
            
            parsed_list = request_builder.get_url().split('/');
            script_name = parsed_list.__getitem__(parsed_list.__len__() - 1)
            
            params_to_request.update({'pg_sig' : sig_helper.make(script_name, params_to_request)})
            response = requests.post(request_builder.get_url(), {'pg_xml' : self.__make_xml_request_from_params(params_to_request)})
                                
            root = fromstring(response.text)
            signature = root.find('pg_sig').text
        except Exception:
            raise SdkException('Cant send request or parse response')
        
        sig_helper = SigHelper(self.secret_key)
        if not sig_helper.check_xml(signature, script_name, response.text):
            raise SdkException('Wrong signature in response')
        
        for child in root:
            if child.tag == 'pg_error_description':
                pg_error_description = child.text
            if child.tag == 'pg_error_code':
                pg_error_code = child.text
                
        if 'pg_error_code' in locals():
            raise SdkException('Error in response ' + pg_error_description + ' code ' + pg_error_code)
        
        return response.text
    
    def __make_xml_request_from_params(self, params):
        request_element = Element('request')
        
        for key in params.keys():
            some_element = SubElement(request_element, str(key))
            some_element.text = str(params.get(str(key)))
   
        request = tostring(request_element, encoding='utf8', method='xml').decode("utf-8")
        
        return request
