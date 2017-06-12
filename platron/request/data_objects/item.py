from platron.request.data_objects.data_object import DataObject
from platron.sdk_exception import SdkException

class Item(DataObject):
    '''
    Item for receipt
    '''

    def __init__(self, label, price, quantity):
        """
        Args:
            label (string): product label
            price (string): price of 1 product
            quantity (string): count of product
        """
        self.pg_label = label
        self.pg_price = price
        self.pg_quantity = quantity
        
    def add_vat(self, vat):
        """
        If not seted vat = non used
        Args:
            vat (string): product vat 0|10|18|110|118
        """
        if self.__get_vat_variables().get(vat) == None:
            raise SdkException('Wrong vat. Use from constants')
            
        self.pg_vat = vat
        return self
    
    def add_amount(self, amount):
        """
        If price * quantity != amount looks like discount
        Args:
            vat (string): product vat from constant
        """      
        self.pg_amount = amount
        return self
        
    def __get_vat_variables(self):
        return {'0' : True,'10' : True,'18' : True,'110' : True,'118' : True}
        