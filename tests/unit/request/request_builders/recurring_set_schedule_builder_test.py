import unittest
from platron.request.request_builders.recurring_set_schedule_buider import RecurringSetScheduleBuilder
from platron.sdk_exception import SdkException


class RecurringSetScheduleBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = RecurringSetScheduleBuilder('12345', '100')
        builder.add_template('2018-01-01', 'week', '10', '100')
        builder.add_dates({'2018-10-10', '2019-10-10'})

        params = builder.get_params()
        template = params.get('pg_template')

        self.assertEquals('12345', params.get('pg_recurring_profile'))
        self.assertEquals('2018-01-01', template.get('pg_start_date'))
        self.assertEquals('week', template.get('pg_interval'))
        self.assertEquals('10', template.get('pg_period'))
        self.assertEquals('100', template.get('pg_max_periods'))
        self.assertTrue({'2018-10-10'}.issubset(params.get('pg_dates')))

        with self.assertRaises(SdkException):
            builder.add_template('2018-01-01', 'wrong_interval', '10', '100')
