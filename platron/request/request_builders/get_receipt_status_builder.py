from platron.request.request_builders.request_builder import RequestBuilder


class GetReceiptStatusBuilder(RequestBuilder):

    def __init__(self, receipt):
        """
        :param receipt: digital platron receipt id (string)
        """
        self.pg_receipt_id = receipt

    def get_url(self):
        return self.PLATRON_URL + 'get_receipt_status.php'
