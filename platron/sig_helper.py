import hashlib
import xml.etree.ElementTree


class SigHelper(object):
    '''
    Class to help make and check sign
    '''

    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.flat_array = {}
        self.flat_xml_array = {}

    def __make_flat_params_xml(self, xml_str, parent_name=''):
        if parent_name == '':
            root = xml.etree.ElementTree.fromstring(xml_str)
        else:
            root = xml_str

        i = 0
        for child in root:

            i += 1
            if child.tag == 'pg_sig':
                continue

            name = parent_name + child.tag + "{:03d}".format(i)
            if self.flat_xml_array.get(name) is not None:
                name = name + '_doubled'

            if list(child):
                self.__make_flat_params_xml(child, name)
                continue

            if child.text is None:
                self.flat_xml_array.update({name: ''})
            else:
                self.flat_xml_array.update({name: child.text})

        return self.flat_xml_array

    def __make_flat_params_array(self, params, parent_name=''):
        i = 0
        for key in params:

            i += 1
            if key == 'pg_sig':
                continue

            name = parent_name + str(key) + "{:03d}".format(i)
            if type(params.get(str(key))) == dict:
                self.__make_flat_params_array(params.get(str(key)), name)
                continue

            self.flat_array.update({key: params.get(str(key))})

        return self.flat_array

    def __make_sig_str(self, script_name, params):
        params.pop('pg_sig', 'deleted')
        list_to_sort = list(params.keys());
        list_to_sort.sort()
        str_to_sig = script_name + ';'

        for key in list_to_sort:
            str_to_sig += str(params.get(str(key))) + ';'

        str_to_sig += self.secret_key
        return str_to_sig

    def make(self, script_name, params):
        """ Make signature by params and script_name
        Args:
            script_name (str): requested script name
            params (dict): params to request
        Returns:
            Signature string
        """
        flat_params = self.__make_flat_params_array(params)
        self.flat_array = {}
        return hashlib.md5(self.__make_sig_str(script_name, flat_params).encode('utf-8')).hexdigest()

    def check(self, signature, script_name, params):
        """ Check signature by params and script_name
        Args:
            signature (str): signature in request to check
            script_name (str): requested script name
            params (dict): params to request
        Returns:
            Boolean
        """
        return signature == self.make(script_name, params)

    def check_xml(self, signature, script_name, xml):
        """ Check signature by params and script_name in xml request string
        Args:
            signature (str): signature in request to check
            script_name (str): requested script name
            xml (str): xml string
        Returns:
            Boolean
        """
        return signature == self.make_xml(script_name, xml)

    def make_xml(self, script_name, xml):
        """ Make signature for xml string
        Args:
            script_name (str): requested script name
            xml (str): xml string
        Returns:
            string
        """
        flat_params = self.__make_flat_params_xml(xml)
        self.flat_xml_array = {}
        return self.make(script_name, flat_params)
