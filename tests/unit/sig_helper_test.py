import unittest
from platron.sig_helper import SigHelper
from xml.etree.ElementTree import Element, SubElement, tostring


class SigHelperTest(unittest.TestCase):

    def setUp(self):
        self.sig_helper = SigHelper('rofoneqaxujagexi')

    def test_make(self):
        self.assertEqual(self.sig_helper.make('payment.php', {'test': 'test1', 'test2': 'test3'}),
                         '27a5edfcb35e2fa44c9adef6994af3f0')

    def test_check(self):
        self.assertTrue(self.sig_helper.check('27a5edfcb35e2fa44c9adef6994af3f0', 'payment.php',
                                              {'test': 'test1', 'test2': 'test3'}))
        self.assertTrue(self.sig_helper.check('fcb6df9c160e55849cc85f5781591b41', 'payment.php',
                                              {'foo': {'1': 'test', '2': 'test2'}}))

    def test_make_xml(self):
        response_element = Element('response')
        description_element = SubElement(response_element, 'pg_description')
        description_element.text = 'test'

        response = tostring(response_element, encoding='utf8', method='xml').decode("utf-8")

        self.assertEqual(self.sig_helper.make_xml('test.php', response), '7e3123d36e6aa859f40dbe4d7eff7c34')
