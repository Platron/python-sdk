import unittest
from platron.request.data_objects.item import Item
from platron.sdk_exception import SdkException


class ItemTest(unittest.TestCase):

    def test_get_params(self):
        data_object = Item('test', '100.00', '2')
        data_object.add_vat('0')
        data_object.add_amount('180.00')
        data_object.add_type('product')

        params = data_object.get_params()

        self.assertEqual('test', params.get('pg_label'))
        self.assertEqual('100.00', params.get('pg_price'))
        self.assertEqual('2', params.get('pg_quantity'))
        self.assertEqual('0', params.get('pg_vat'))
        self.assertEqual('180.00', params.get('pg_amount'))
        self.assertEqual('product', params.get('pg_type'))

        with self.assertRaises(SdkException):
            data_object.add_vat('wrong_vat')
