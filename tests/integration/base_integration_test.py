import unittest

from .merchant_settings import MerchantSettings


class BaseIntegrationTest(unittest.TestCase):

    def get_merchant_id(self):
        return MerchantSettings.MERCHANT_ID

    def get_secret_key(self):
        return MerchantSettings.SECRET_KEY
