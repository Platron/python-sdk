from xml.etree.ElementTree import fromstring

from .base_integration_test import BaseIntegrationTest
from platron.request.clients.post_client import PostClient
from platron.request.request_builders.receipt_builder import ReceiptBuilder
from platron.request.data_objects.item import Item
from platron.request.request_builders.init_payment_builder import InitPaymentBuilder


class ReceiptTest(BaseIntegrationTest):

    def test_create_transaction_chain(self):
        builder = InitPaymentBuilder('20.00', 'test')
        client = PostClient(self.get_merchant_id(), self.get_secret_key())
        result = client.request(builder)
        root = fromstring(result)
        pg_payment_id = root.find('pg_payment_id').text

        builder = ReceiptBuilder('payment', pg_payment_id)
        builder.add_additional_payment('credit', '20')

        receipt_item = Item('test', '30.00', '1')
        receipt_item.add_agent('commissionaire', 'test agent', '7707357618', '79050000000')
        receipt_item.add_vat('0')
        receipt_item.add_payment_type('pre_payment_full')
        receipt_item.add_nomenclature_code('44h4Dh04h2Fh1Fh96h81h78h4Ah67h58h4Ah35h2Eh54h31h31h32h30h30h30h')

        builder.add_item(receipt_item)
        builder.add_additional_payment('credit', '10.00')

        self.assertIsNotNone(client.request(builder))
