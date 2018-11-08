import unittest
from platron.request.request_builders.create_moneyback_builder import CreateMoneybackBuilder


class CreateMoneybackBuilderTest(unittest.TestCase):

    def test_get_parameters(self):
        builder = CreateMoneybackBuilder('346536', 'YANDEXMONEY_O', '10.00', 'test',
                                         {'destination_account': '3454353453543'})
        builder.bind_to_transaction('3453523')
        params = builder.get_params()

        self.assertEqual('346536', params.get('pg_contract_id'))
        self.assertEqual('YANDEXMONEY_O', params.get('pg_moneyback_system'))
        self.assertEqual('10.00', params.get('pg_amount'))
        self.assertEqual('test', params.get('pg_description'))
        self.assertEqual('3454353453543', params.get('destination_account'))
        self.assertEqual('3453523', params.get('pg_payment_id'))
