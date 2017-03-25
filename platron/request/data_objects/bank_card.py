from platron.request.data_objects.data_object import DataObject

class BankCard(DataObject):
    '''
    Bank card data to send init_payment - only to merchants, whicj have PCI DSS
    '''

    def __init__(self, card_number, card_holder_name, exp_year, exp_month, cvv, user_ip):
        self.pg_card_number = card_number
        self.pg_user_cardholder = card_holder_name
        self.pg_exp_year = exp_year
        self.pg_exp_month = exp_month
        self.pg_cvv2 = cvv
        self.user_ip = user_ip