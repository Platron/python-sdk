from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException


class RecurringSetScheduleBuilder(RequestBuilder):

    dates = []

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
        :param dates: Set of sting dates
        """
        if dates.len(dates) == 0:
            raise SdkException('Use not empty Set')

        self.dates.append(dates)

    def add_template(self, start_date, interval, period, max_periods=None):
        """
        :param start_date: start date of template (string)
        :param interval: day|week|month (string)
        :param period: digital period of interval (string)
        :param max_periods: digital max periods (string)
        """
        if self.__get_intervals().get(interval) == None:
            raise SdkException('Wrong interval. Use from constants')

        self.pg_start_date = start_date
        self.pg_interval = interval
        self.pg_period = period

        if max_periods != None:
            self.pg_max_periods = max_periods

    def item_function(self, parent):
        return 'pg_dates'

    def after_xml_created(self, xml):
        return xml.replace('<pg_dates>', '').replace('</pg_dates>', '')

    def __get_intervals(self):
        return {'day': True, 'week': True, 'month': True}
