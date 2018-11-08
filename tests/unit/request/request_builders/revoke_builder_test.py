import unittest
from platron.request.request_builders.revoke_builder import RevokeBuilder


class RevokeBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = RevokeBuilder('3444223')
        builder.set_amount('10.00')
        parameters = builder.get_params()

        self.assertEqual('3444223', parameters.get('pg_payment_id'))
        self.assertEqual('10.00', parameters.get('pg_refund_amount'))
