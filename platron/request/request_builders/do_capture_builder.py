from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException
from platron.request.data_objects.long_record import LongRecord

class DoCaptureBuilder(RequestBuilder):
    '''
    Do capture API request
    '''

    def __init__(self, payment):
        self.pg_payment_id = payment
       
    def add_long_record(self, long_record):
        if type(long_record) != LongRecord:
            raise SdkException('Only long record object expected')
        
        for param_name in long_record.keys():
            setattr(self, param_name, long_record.get(param_name))
            
        return self
    
    def get_url(self):
        return self.PLATRON_URL + 'do_capture.php' 