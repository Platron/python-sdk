import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

from platron.request.data_objects.avia_gds import AviaGds
from platron.request.data_objects.bank_card import BankCard
from platron.request.request_builders.init_payment_builder import InitPaymentBuilder
from platron.sdk_exception import SdkException

class InitPaymentBuiderTest(unittest.TestCase):
    '''
    Init payment builder test
    '''

    def test_get_params(self):
        builder = InitPaymentBuilder('10.00', 'test')
        builder.add_capture_url('www.site.ru/capture.php')
        builder.add_check_url('www.site.ru/check.php')
        builder.add_currency('RUB')
        builder.add_failure_url('www.site.ru/failure.php')
        builder.add_failure_url_method('POST')
        builder.add_lifetime('604800')
        builder.add_merchant_params({'merchant_param' : 'test'})
        builder.add_order_id('555')
        builder.add_payment_system('RUSSIANSTANDARD')
        builder.add_postpone()
        builder.add_ps_additional_parameters({'pg_alfaclick_client_id' : '111333'})
        builder.add_recurring_start()
        builder.add_refund_url('www.site.ru/refund.php')
        builder.add_request_method('POST')
        builder.add_result_url('www.site.ru/result.php')
        builder.add_site_url('www.site.ru')
        builder.add_state_url('www.site.ru/state.php')
        builder.add_state_url_method('POST')
        builder.add_success_url('www.site.ru/success.php')
        builder.add_success_url_method('POST')
        builder.add_testing_mode()
        builder.add_user_email('test@test.ru')
        builder.add_user_ip('62.213.64.221')
        builder.add_user_phone('79268750000')
        
        bankcardStub = Mock(spec=BankCard)
        bankcardStub.get_params = MagicMock(return_value={'bank_card_test' : 'bank_card_test'})
        
        aviaGdsStub = Mock(spec=AviaGds)
        aviaGdsStub.get_params = MagicMock(return_value={'gds_test' : 'gds_test'})
        
        builder.add_bankcard(bankcardStub)
        builder.add_gds(aviaGdsStub)
        
        parameters = builder.get_params()
        
        self.assertEqual('www.site.ru/capture.php', parameters.get('pg_capture_url'))
        self.assertEqual('www.site.ru/check.php', parameters.get('pg_check_url'))
        self.assertEqual('RUB', parameters.get('pg_currency'))
        self.assertEqual('www.site.ru/failure.php', parameters.get('pg_failure_url'))
        self.assertEqual('POST', parameters.get('pg_failure_url_method'))
        self.assertEqual('604800', parameters.get('pg_lifetime'))
        self.assertEqual('test', parameters.get('merchant_param'))
        self.assertEqual('555', parameters.get('pg_order_id'))
        self.assertEqual('RUSSIANSTANDARD', parameters.get('pg_payment_system'))
        self.assertEqual(1, parameters.get('pg_postpone'))
        self.assertEqual('111333', parameters.get('pg_alfaclick_client_id'))
        self.assertEqual(1, parameters.get('pg_recurring_start'))
        self.assertEqual('www.site.ru/refund.php', parameters.get('pg_refund_url'))
        self.assertEqual('POST', parameters.get('pg_request_method'))
        self.assertEqual('www.site.ru/result.php', parameters.get('pg_result_url'))
        self.assertEqual('www.site.ru', parameters.get('pg_site_url'))
        self.assertEqual('www.site.ru/state.php', parameters.get('pg_state_url'))
        self.assertEqual('POST', parameters.get('pg_state_url_method'))
        self.assertEqual('www.site.ru/success.php', parameters.get('pg_success_url'))
        self.assertEqual('POST', parameters.get('pg_success_url_method'))
        self.assertEqual(1, parameters.get('pg_testing_mode'))
        self.assertEqual('test@test.ru', parameters.get('pg_user_contact_email'))
        self.assertEqual('62.213.64.221', parameters.get('pg_user_ip'))
        self.assertEqual('79268750000', parameters.get('pg_user_phone'))
        
        self.assertEqual('bank_card_test', parameters.get('bank_card_test'))
        self.assertEqual('gds_test', parameters.get('gds_test'))

        with self.assertRaises(SdkException):
            builder.add_merchant_params({'pg_wrong_merchant_param' : 'test'})
            
        with self.assertRaises(SdkException):
            builder.add_ps_additional_parameters({'wrong_ps_param' : 'test'})   
        
        
        