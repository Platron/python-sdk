from platron.request.request_builders.request_builder import RequestBuilder


class RecurringClearScheduleBuilder(RequestBuilder):

    def __init__(self, recurring_profile):
        """
        :param recurring_profile: recurring id
        """
        self.pg_recurring_profile = recurring_profile

    def get_url(self):
        return self.PLATRON_URL + 'index.php/api/recurring/clear-schedule'
