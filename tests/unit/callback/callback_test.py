import unittest
from platron.callback.callback import Callback
import xml.etree.ElementTree

class CallbackTest(unittest.TestCase):
    '''
    Test callback class
    '''

    def setUp(self):
        self.callback = Callback('test.php', 'adfsvsdfvsd')
        
    def test_ok_answear(self):
        xml_string = self.callback.response_ok({'pg_salt' : '1111'})
        root = xml.etree.ElementTree.fromstring(xml_string)
        
        self.assertEqual(root.find('pg_status').text, 'ok')
        self.assertTrue(root.find('pg_sig').text)
        self.assertTrue(root.find('pg_description').text)
        self.assertTrue(root.find('pg_salt').text)
        
    def test_error_answear(self):
        xml_string = self.callback.response_error({'pg_salt' : '1111'}, 'some_error')
        root = xml.etree.ElementTree.fromstring(xml_string)
        
        self.assertEqual(root.find('pg_status').text, 'error')
        self.assertTrue(root.find('pg_sig').text)
        self.assertTrue(root.find('pg_description').text)
        self.assertTrue(root.find('pg_salt').text)
        
    def test_rejected_answear(self):
        xml_string = self.callback.response_rejected({'pg_salt' : '1111'}, 'reject please')
        root = xml.etree.ElementTree.fromstring(xml_string)
        
        self.assertEqual(root.find('pg_status').text, 'rejected')
        self.assertTrue(root.find('pg_sig').text)
        self.assertTrue(root.find('pg_description').text)
        self.assertTrue(root.find('pg_salt').text)
        
    def test_can_reject(self):
        self.assertTrue(self.callback.can_reject({'pg_can_reject' : '1'}))
        self.assertFalse(self.callback.can_reject({'pg_can_reject' : '0'}))
        self.assertFalse(self.callback.can_reject({}))