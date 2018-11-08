import unittest
from platron.request.request_builders.recurring_get_schedule_builder import RecurringGetScheduleBuilder


class RecurringGetScheduleBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = RecurringGetScheduleBuilder('12345')

        params = builder.get_params()
        self.assertEquals('12345', params.get('pg_recurring_profile'))
