from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException


class RecurringSetScheduleBuilder(RequestBuilder):

    def __init__(self, recurring_profile, amount):
        """
        :param recurring_profile: digital recurring profile id (string)
        :param amount: amount of future transactions (string)
        """
        self.pg_recurring_profile = recurring_profile
        self.pg_amount = amount

    def get_url(self):
        return self.PLATRON_URL + 'index.php/api/recurring/set-schedule'

    def add_dates(self, dates):
        """
        :param dates: Set of sting dates (Dict)
        """
        if len(dates) == 0:
            raise SdkException('Use not empty Set')

        self.pg_dates = dates

    def add_template(self, start_date, interval, period, max_periods=None):
        """
        :param start_date: start date of template (string)
        :param interval: day|week|month (string)
        :param period: digital period of interval (string)
        :param max_periods: digital max periods (string)
        """
        if self.__get_intervals().get(interval) == None:
            raise SdkException('Wrong interval. Use from constants')

        self.pg_template = {'pg_start_date': start_date, 'pg_interval': interval, 'pg_period': period}
        if max_periods != None:
            self.pg_template.update({'pg_max_periods': max_periods})

    @staticmethod
    def __get_intervals():
        return {'day': True, 'week': True, 'month': True}
