import unittest
from platron.request.clients.post_client import PostClient
from platron.sdk_exception import SdkException

class PostClientTest(unittest.TestCase):
    '''
    Testing post client
    '''

    def test_request(self):        
        data_object1 = DataObject1()
        data_object2 = DataObject2()
        
        with self.assertRaises(SdkException):
            client1 = PostClient('82', 'sdcacsdcasdc')
            client1.request(data_object1)                        
            
        with self.assertRaises(SdkException):
            client2 = PostClient('82', 'sdcacsdcasdc')
            client2.request(data_object2)
                
class DataObject1(object):
    def get_params(self):
        return {}
    
    def get_url(self):
        return 'www.platron.ru/get_registry.php'
    
class DataObject2(object):
    def get_params(self):
        return {'test1' : 'test2'}
    
    def get_url(self):
        return 'www.google.com'