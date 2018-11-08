import unittest
from platron.request.request_builders.recurring_clear_schedule_builder import RecurringClearScheduleBuilder


class RecurringClearScheduleBuilderTest(unittest.TestCase):

    def test_get_params(self):
        builder = RecurringClearScheduleBuilder('12345')

        params = builder.get_params()
        self.assertEquals('12345', params.get('pg_recurring_profile'))
