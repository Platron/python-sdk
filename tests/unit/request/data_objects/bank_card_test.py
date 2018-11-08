import unittest
from platron.request.data_objects.bank_card import BankCard


class BankCardTest(unittest.TestCase):

    def test_get_parameters(self):
        data_object = BankCard('4256000000000003', 'alexey lashnev', '2020', '01', '777', '62.213.64.221')
        params = data_object.get_params()

        self.assertEqual('4256000000000003', params.get('pg_card_number'))
        self.assertEqual('alexey lashnev', params.get('pg_user_cardholder'))
        self.assertEqual('2020', params.get('pg_exp_year'))
        self.assertEqual('01', params.get('pg_exp_month'))
        self.assertEqual('777', params.get('pg_cvv2'))
        self.assertEqual('62.213.64.221', params.get('pg_user_ip'))
