from .base_integration_test import BaseIntegrationTest
from platron.request.request_builders.ps_list_builder import PsListBuilder
from platron.request.clients.post_client import PostClient


class PsListTest(BaseIntegrationTest):

    def test_ps_list(self):
        builder = PsListBuilder('10.00')
        client = PostClient(self.get_merchant_id(), self.get_secret_key())

        self.assertIsNotNone(client.request(builder))
