from .client import Client

class PostClient(Client):
    '''
    Send request to platron by post
    '''


    def __init__(self, merchant, secret_key):
        self.merchant = merchant
        self.secret_key = secret_key
    
    def request(self, request_builder):
        return None