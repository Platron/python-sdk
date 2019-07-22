from platron.request.data_objects.data_object import DataObject
from platron.sdk_exception import SdkException


class Item(DataObject):

    def __init__(self, label, price, quantity):
        """
        Args:
            :param label: product label (string)
            :param price: price of 1 product (string)
            :param quantity: count of product (string)
        """
        self.pg_label = label
        self.pg_price = price
        self.pg_quantity = quantity

    def add_vat(self, vat):
        """
        :param vat: product vat 0|10|20|110|120 (string)
        """
        if self.__get_vat_variables().get(vat) == None:
            raise SdkException('Wrong vat. Use from constants')

        self.pg_vat = vat

    def add_amount(self, amount):
        """
        Add amount to receipt item
        Args:
            amount (float): product amount
        """
        self.pg_amount = amount

    def add_type(self, item_type):
        """
        :param item_type: product type (string)
        """
        if self.__get_type_variables().get(item_type) == None:
            raise SdkException('Wrong item type. Use from constants')

        self.pg_type = item_type

    def add_payment_type(self, payment_type):
        """
        :param payment_type: payment type (string)
        """
        if self.__get_payment_type_variables().get(payment_type) == None:
            raise SdkException('Wrong item type. Use from constants')

        self.pg_payment_type = payment_type

    def add_agent(self, agent_type, agent_name, agent_inn, agent_phone):
        """
        :param agent_type: agent type (string)
        :param agent_name: agent name (string)
        :param agent_inn: agent inn (string)
        :param agent_phone: agent legal phone sample 79050000000 (string)
        """
        if self.__get_agent_type_variables().get(agent_type) == None:
            raise SdkException('Wrong item type. Use from constants')

        self.pg_agent_type = agent_type
        self.pg_agent_name = agent_name
        self.pg_agent_inn = agent_inn
        self.pg_agent_phone = agent_phone

    @staticmethod
    def __get_vat_variables():
        return {'0': True, '10': True, '20': True, '110': True, '120': True}

    @staticmethod
    def __get_type_variables():
        return {'product': True, 'product_excise': True, 'work': True, 'service': True, 'gambling_bet': True,
                'gambling_win': True, 'lottery_bet': True, 'lottery_win': True, 'rid': True, 'payment': True,
                'commission': True, 'composite': True, 'other': True}

    @staticmethod
    def __get_payment_type_variables():
        return {'full_payment': True, 'pre_payment_full': True, 'pre_payment_part': True, 'advance': True,
                'credit_part': True, 'credit_pay': True, 'credit': True}

    @staticmethod
    def __get_agent_type_variables():
        return {'commissionaire': True}
