from platron.request.request_builders.init_payment_builder import InitPaymentBuilder
from platron.request.clients.post_client import PostClient

client = PostClient('82', 'sdcacsdcasdc')
init_payment_builder = InitPaymentBuilder('10.00', 'test')
print(client.request(init_payment_builder))