from platron.request.data_objects.data_object import DataObject


class AviaGds(DataObject):

    def __init__(self, rec_loc, gds, markup):
        """
        :param rec_loc: PNR in GDS - 6 character (string)
        :param gds: GDS name (SABRE|GALILEO|AMADEUS) (string)
        :param markup: merchant markup amount (string)
        """
        self.pg_rec_log = rec_loc
        self.pg_gds = gds
        self.pg_merchant_markup = markup

    def add_card_brands(self, card_brands):
        """
        :param card_brands: VI|CA|MI etc. (Dict)
        """
        self.pg_card_brand = card_brands
