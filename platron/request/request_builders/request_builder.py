import abc
from platron.sdk_exception import SdkException


class RequestBuilder(metaclass=abc.ABCMeta):

    PLATRON_URL = 'https://www.platron.ru/'

    def get_url(self):
        raise SdkException('Not implemented get_url method')

    def get_params(self):
        """
        :return: params to request (Dict)
        """
        params = [arg for arg in dir(self) if not arg.startswith('_')]
        callable_params = [arg for arg in dir(self) if callable(getattr(self, arg)) and not arg.startswith('_')]

        params.remove('PLATRON_URL')
        for callable_param in callable_params:
            params.remove(callable_param)

        params_to_request = {}
        for param_name in params:
            params_to_request.update({param_name: getattr(self, param_name)})

        return params_to_request

    def item_function(self, parent):
        """
        Как будут называться элементы, не имеющие названия - set()
        """
        return 'item'

    def after_xml_created(self, xml):
        """
        Постобработка xml
        """
        return xml
