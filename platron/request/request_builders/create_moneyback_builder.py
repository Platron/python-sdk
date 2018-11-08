from platron.request.request_builders.request_builder import RequestBuilder


class CreateMoneybackBuilder(RequestBuilder):

    def __init__(self, contract, moneyback_system, amount, description, ps_additional_params):
        """
        :param contract: merchant contract which he get from MoneybackSystemListBuilder (string)
        :param moneyback_system: moneyback payment system from MoneybackSystemListBuilder (string)
        :param amount: amount to moneyback (string)
        :param description: reason of moneyback (string)
        :param ps_additional_params: params which need to concrete moneyback system from MoneybackSystemListBuilder (Dict)
        """
        self.pg_contract_id = contract
        self.pg_moneyback_system = moneyback_system
        self.pg_amount = amount
        self.pg_description = description
        for ps_param_name in ps_additional_params.keys():
            setattr(self, ps_param_name, ps_additional_params.get(ps_param_name))

    def get_url(self):
        return self.PLATRON_URL + 'create_moneyback.php'

    def bind_to_transaction(self, payment):
        """
        :param payment: digital platron payment id (string)
        """
        self.pg_payment_id = payment
