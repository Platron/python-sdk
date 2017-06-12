import requests
import random
import dicttoxml
from xml.etree.ElementTree import fromstring

from platron.request.clients.platron_client import PlatronClient
from platron.sig_helper import SigHelper
from platron.sdk_exception import SdkException

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
            
            not_treated_xml = dicttoxml.dicttoxml(params_to_request, True, 'request', False, False, item_func=request_builder.item_function)
            xml_to_request_no_sig = request_builder.after_xml_created(not_treated_xml.decode('utf_8'))
            signature = sig_helper.make_xml(script_name, xml_to_request_no_sig)
            xml_to_request = self.add_sig_to_xml(xml_to_request_no_sig, signature)
            print(xml_to_request)

            response = requests.post(request_builder.get_url(), {'pg_xml' : xml_to_request})
            root = fromstring(response.text)
            signature = root.find('pg_sig').text
        except Exception:
            raise SdkException('Cant send request or parse response')
                
        for child in root:
            if child.tag == 'pg_error_description':
                pg_error_description = child.text
            if child.tag == 'pg_error_code':
                pg_error_code = child.text
                
        if 'pg_error_code' in locals():
            raise SdkException('Error in response ' + pg_error_description + ' code ' + pg_error_code)
                
        sig_helper = SigHelper(self.secret_key)
        if not sig_helper.check_xml(signature, script_name, response.text):
            raise SdkException('Wrong signature in response')
        
        return response.text
    
    def add_sig_to_xml(self, xml, sig):
        return xml.replace('</request>','<pg_sig>'+ sig +'</pg_sig></request>')