from platron.sig_helper import SigHelper
from platron.sdk_exception import SdkException
from xml.etree.ElementTree import Element, SubElement, tostring

class Callback(object):
    '''
    Callback helper to process request from platron
    '''

    def __init__(self, script_name, secret_key):
        """
        Args:
            script_name (string): requested string
            secret_key (string): merchant secret key from https://www.platron.ru/admin/merchants.php
        """
        self.script_name = script_name
        self.sig_helper = SigHelper(secret_key)
        
    def __response(self, salt, status, description):
        response_element = Element('response')
        
        status_element = SubElement(response_element, 'pg_status')
        status_element.text = status
        
        salt_element = SubElement(response_element, 'pg_salt')
        salt_element.text = salt
        
        description_element = SubElement(response_element, 'pg_description')
        description_element.text = description
        
        signature = self.sig_helper.make_xml(self.script_name, tostring(response_element))
        
        signature_element = SubElement(response_element, 'pg_sig')
        signature_element.text = signature
        
        return tostring(response_element)
    
    def validate_sig(self, params):
        """ Validete signature in callback request
        Args:
            params (dict): xml string
        Returns:
            Boolean
        """
        try :
            pg_sig = params.get('pg_sig')
        except Exception:
            raise SdkException('No pg_sig in request')    
        
        return self.sig_helper.check(pg_sig, self.script_name, params)
    
    def response_error(self, params, error):
        """ Get xml with error to responde
        Args:
            params (dict): xml string
            error (str): error description
        Returns:
            Xml string
        """
        try :
            pg_salt = params.get('pg_salt')
        except Exception:
            raise SdkException('No pg_salt in request')
        
        return self.__response(pg_salt, 'error', error)
    
    def response_ok(self, params):
        """ Get xml with ok to responde
        Args:
            params (dict): xml string
        Returns:
            Xml string
        """
        try :
            pg_salt = params.get('pg_salt')
        except Exception:
            raise SdkException('No pg_salt in request')
        
        return self.__response(pg_salt, 'ok', 'ok')
    
    def response_rejected(self, params, description):
        """ Get xml with rejected to responde
        Args:
            params (dict): xml string
            error (str): rejected description
        Returns:
            Xml string
        """
        try :
            pg_salt = params.get('pg_salt')
        except Exception:
            raise SdkException('No pg_salt in request')
        
        return self.__response(pg_salt, 'rejected', description)
    
    def can_reject(self, params):
        """ Can reject payment or not
        Args:
            params (dict): xml string
        Returns:
            Boolean
        """
        try :
            can_reject = params.get('pg_can_reject')
        except Exception:
            return 0
        
        return can_reject