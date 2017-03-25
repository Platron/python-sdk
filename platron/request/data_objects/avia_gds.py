from platron.request.data_objects.data_object import DataObject

class AviaGds(DataObject):
    '''
    Avia GDS data for init_payment request
    '''

    def __init__(self, rec_loc, gds, markup):
        self.pg_rec_log = rec_loc
        self.pg_gds = gds
        self.pg_merchant_markup = markup
        
    def add_card_brands(self, card_brands):
        self.pg_card_brand = card_brands