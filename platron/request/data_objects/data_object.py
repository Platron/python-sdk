import abc

class DataObject(metaclass=abc.ABCMeta):
    '''
    Base data object class
    '''

    def get_params(self):
        params = [arg for arg in dir(self) if not arg.startswith('_')]
        callable_params = [arg for arg in dir(self) if callable(getattr(self, arg)) and not arg.startswith('_')]
        
        params.remove('PLATRON_URL')
        for callable_param in callable_params:
            params.remove(callable_param)
            
        params_to_request = {}
        for param_name in params:
            params_to_request.update({param_name : getattr(self, param_name)})
            
        return params_to_request