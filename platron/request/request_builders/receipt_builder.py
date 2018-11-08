from platron.request.request_builders.request_builder import RequestBuilder
from platron.sdk_exception import SdkException
from platron.request.data_objects.item import Item


class ReceiptBuilder(RequestBuilder):

    receipt_items = []

    def __init__(self, operation_type, payment_id=None, order_id=None):
        """
        Payment id or order id is not None
        :param operation_type: operation type payment|refund|moneyback (string)
        :param payment_id: digital platron payment id (string)
        :param order_id: merchant order id (string)
        """
        if payment_id == None and order_id == None:
            raise SdkException('payment id or order id must be nut null')

        if self.__get_operstion_types().get(operation_type) == None:
            raise SdkException('Wrong vat. Use from constants')

        self.pg_operation_type = operation_type
        if payment_id != None:
            self.pg_payment_id = payment_id
        if order_id != None:
            self.pg_order_id = order_id

    def add_additional_payment(self, payment_type, amount):
        """
        :param payment_type: additional payment type credit|debit (string)
        :param amount: additional payment amount (string)
        """
        if self.__get_additional_payment_types().get(payment_type) == None:
            raise SdkException('Wrong additional payment type. Use from constants')

        self.pg_additional_payment_type = payment_type
        self.pg_additional_payment_amount = amount

    def get_url(self):
        return self.PLATRON_URL + 'receipt.php'

    def add_item(self, item):
        """
        :param item: 1 item in receipt (Item)
        """
        if not isinstance(item, Item):
            raise SdkException('Only item object expected')

        self.receipt_items.append(item.get_params())

    @staticmethod
    def __get_operstion_types():
        return {'payment': True, 'refund': True, 'moneyback': True}

    @staticmethod
    def __get_additional_payment_types():
        return {'credit': True, 'debit': True}

    def item_function(self, parent):
        return 'pg_items'

    def after_xml_created(self, xml):
        return xml.replace('<receipt_items>', '').replace('</receipt_items>', '')
