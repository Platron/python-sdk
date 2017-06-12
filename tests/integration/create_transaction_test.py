from .base_integration_test import BaseIntegrationTest
from platron.request.clients.post_client import PostClient
from platron.request.request_builders.init_payment_builder import InitPaymentBuilder

class CreateTransactionTest(BaseIntegrationTest):
    '''
    Интеграционный тест цепочки создание транзакции
    '''
    
    def test_create_transaction(self):
        builder = InitPaymentBuilder('10.00', 'test')
        client = PostClient(self.get_merchant_id(), self.get_secret_key())        
        
        self.assertIsNotNone(client.request(builder))