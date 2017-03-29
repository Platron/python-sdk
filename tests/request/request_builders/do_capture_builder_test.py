import unittest
from platron.request.request_builders.do_capture_builder import DoCaptureBuilder

class DoCaptureBuilderTest(unittest.TestCase):
    '''
    Do capture builder test
    '''

    def test_get_params(self):
        builder = DoCaptureBuilder('343242')
        params = builder.get_params()
        
        self.assertEqual('343242', params.get('pg_payment_id'))