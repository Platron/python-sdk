import requests

from platron.request.clients.platron_client import PlatronClient
from platron.exception import SdkException
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
            response = requests.post(request_builder.get_url(), request_builder.get_params())      
            root = xml.etree.ElementTree.fromstring(response)
        except Exception:
            raise SdkException('Cant send request')

        for child in root:
            if child.tag == 'pg_error':
                pg_error = child.text
            if child.tag == 'pg_error_code':
                pg_error_code = child.text
                
        if pg_error_code:
            raise SdkException('Error in response ' + pg_error + 'code ' + pg_error_code)
        
        return root