from platron.request.data_objects.data_object import DataObject

class AviaGds(DataObject):
    '''
    Avia GDS data for init_payment request
    '''

    def __init__(self, rec_loc, gds, markup):
        """
        Args:
            rec_loc (string): PNR in GDS
            gds (string): GDS (SABRE|GALILEO|AMADEUS)
            markup (string): merchant markup
        """
        self.pg_rec_log = rec_loc
        self.pg_gds = gds
        self.pg_merchant_markup = markup
        
    def add_card_brands(self, card_brands):
        """Add card brand filter which can be used
        Args:
            card_brands (dict): VI|CA|MI etc.
        """
        self.pg_card_brand = card_brands