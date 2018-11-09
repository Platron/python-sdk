from xml.etree.ElementTree import fromstring

from .base_integration_test import BaseIntegrationTest
from platron.request.clients.post_client import PostClient
from platron.request.request_builders.receipt_builder import ReceiptBuilder
from platron.request.data_objects.item import Item
from platron.request.request_builders.init_payment_builder import InitPaymentBuilder


class ReceiptTest(BaseIntegrationTest):

    def test_create_transaction_chain(self):
        builder = InitPaymentBuilder('50.00', 'test')
        client = PostClient(self.get_merchant_id(), self.get_secret_key())
        result = client.request(builder)
        root = fromstring(result)
        pg_payment_id = root.find('pg_payment_id').text

        builder = ReceiptBuilder('payment', pg_payment_id)
        builder.add_additional_payment('credit', '20')

        receipt_item1 = Item('test', '10.00', '1')
        receipt_item1.add_agent('commissionaire', 'test agent', '123456789012', '79050000000')
        receipt_item2 = Item('test2', '20.00', '1')
        receipt_item2.add_agent('commissionaire', 'test agent', '123456789012', '79050000000')

        builder.add_item(receipt_item1)
        builder.add_item(receipt_item2)

        self.assertIsNotNone(client.request(builder))
