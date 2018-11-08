from platron.request.request_builders.request_builder import RequestBuilder


class MoneybackSystemListBuilder(RequestBuilder):

    def __init__(self):
        pass

    def get_url(self):
        return self.PLATRON_URL + 'moneyback_system_list.php'
