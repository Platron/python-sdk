import unittest
from platron.request.data_objects.item import Item
from platron.sdk_exception import SdkException


class ItemTest(unittest.TestCase):

    def test_get_params(self):
        data_object = Item('test', '100.00', '2')
        data_object.add_vat('0')
        data_object.add_amount('180.00')
        data_object.add_type('product')
        data_object.add_payment_type('full_payment')
        data_object.add_agent('commissionaire', 'test agent', '123456789012', '79000000000')
        data_object.add_nomenclature_code('44h4Dh04h2Fh1Fh96h81h78h4Ah67h58h4Ah35h2Eh54h31h31h32h30h30h30h')

        params = data_object.get_params()

        self.assertEqual('test', params.get('pg_label'))
        self.assertEqual('100.00', params.get('pg_price'))
        self.assertEqual('2', params.get('pg_quantity'))
        self.assertEqual('0', params.get('pg_vat'))
        self.assertEqual('180.00', params.get('pg_amount'))
        self.assertEqual('product', params.get('pg_type'))
        self.assertEqual('full_payment', params.get('pg_payment_type'))
        self.assertEqual('commissionaire', params.get('pg_agent_type'))
        self.assertEqual('test agent', params.get('pg_agent_name'))
        self.assertEqual('123456789012', params.get('pg_agent_inn'))
        self.assertEqual('79000000000', params.get('pg_agent_phone'))
        self.assertEqual('44h4Dh04h2Fh1Fh96h81h78h4Ah67h58h4Ah35h2Eh54h31h31h32h30h30h30h', params.get('pg_nomenclature_code'))

        with self.assertRaises(SdkException):
            data_object.add_vat('wrong_vat')
        with self.assertRaises(SdkException):
            data_object.add_agent('wrong_agent_type', 'test agent', '123456789012', '79000000000')
        with self.assertRaises(SdkException):
            data_object.add_payment_type('wrong_payment_type')
        with self.assertRaises(SdkException):
            data_object.add_type('wrong_type')
