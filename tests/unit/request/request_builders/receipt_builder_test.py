import unittest
from unittest.mock import Mock

from platron.request.request_builders.receipt_builder import ReceiptBuilder
from platron.sdk_exception import SdkException
from platron.request.data_objects.item import Item


class PsListBuilderTest(unittest.TestCase):

    def test_get_params(self):
        item_stub = Mock(spec=Item)
        builder = ReceiptBuilder('payment', '100500', 'abc1')
        builder.add_item(item_stub)

        parameters = builder.get_params()

        self.assertEqual('payment', parameters.get('pg_operation_type'))
        self.assertEqual('100500', parameters.get('pg_payment_id'))
        self.assertEqual('abc1', parameters.get('pg_order_id'))

        with self.assertRaises(SdkException):
            builder.add_item({'pg_wrong_item': 'test'})

        with self.assertRaises(SdkException):
            ReceiptBuilder('payment')

        with self.assertRaises(SdkException):
            ReceiptBuilder('wrong_item')
