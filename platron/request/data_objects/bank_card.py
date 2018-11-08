from platron.request.data_objects.data_object import DataObject


class BankCard(DataObject):

    def __init__(self, card_number, card_holder_name, exp_year, exp_month, cvv, user_ip):
        """
        Args:
            :param card_number: card number (string)
            :param card_holder_name (string): card holder name (string)
            :param exp_year: card expiration year (string)
            :param exp_month: card expiration month (string)
            :param cvv: card cvv (string)
            :param user_ip: user real ip (string)
        """
        self.pg_card_number = card_number
        self.pg_user_cardholder = card_holder_name
        self.pg_exp_year = exp_year
        self.pg_exp_month = exp_month
        self.pg_cvv2 = cvv
        self.pg_user_ip = user_ip
