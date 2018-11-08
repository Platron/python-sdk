import unittest
from platron.request.request_builders.get_status_builder import GetStatusBuilder


class GetStatusBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = GetStatusBuilder('34442335')
        parameters = builder.get_params()

        self.assertEqual('34442335', parameters.get('pg_payment_id'))

        builder = GetStatusBuilder(None, '4443')
        parameters = builder.get_params()

        self.assertEqual('4443', parameters.get('pg_order_id'))
