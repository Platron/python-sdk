import unittest
from platron.request.request_builders.make_recurring_builder import MakeRecurringBuilder
from platron.sdk_exception import SdkException


class MakeRecurringBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = MakeRecurringBuilder('4321', 'test')
        builder.add_amount('10.00')
        builder.add_encoding('UTF8')
        builder.add_merchant_params({'merchant_param': 'test'})
        builder.add_order_id('777944')
        builder.add_refund_url('www.test.ru/refund.php')
        builder.add_request_method('POST')
        builder.add_result_url('www.test.ru/result.php')

        params = builder.get_params()

        self.assertEqual('4321', params.get('pg_recurring_profile'))
        self.assertEqual('test', params.get('pg_description'))

        self.assertEqual('10.00', params.get('pg_amount'))
        self.assertEqual('UTF8', params.get('pg_encoding'))
        self.assertEqual('test', params.get('merchant_param'))
        self.assertEqual('777944', params.get('pg_order_id'))
        self.assertEqual('www.test.ru/refund.php', params.get('pg_refund_url'))
        self.assertEqual('POST', params.get('pg_request_method'))
        self.assertEqual('www.test.ru/result.php', params.get('pg_result_url'))

        with self.assertRaises(SdkException):
            builder.add_merchant_params({'pg_not_merchant_param': 'test'})
