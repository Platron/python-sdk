import _md5
import xml.etree.ElementTree

class SigHelper(object):
    
    flat_xml_array = {}
    flat_array = {}
    
    '''
    Class to help make and check sign
    '''
    def __init__(self, secret_key):
        self.secret_key = secret_key
        
    def __make_flat_params_xml(self, xml, parent_name = None):
        if parent_name == None:
            root = xml.etree.ElementTree.fromstring(xml)
        
        i = 0
        for child in root:
            if child.text == 'pg_sig':
                continue
            
            name = parent_name + child.tag + str(i)
            
            if child.getchildren() == []:
                self.__make_flat_params_xml(xml, name)
                continue
            
            self.flat_xml_array.update({name : child.text})
            
        return self.flat_xml_array
        
    def __make_flat_params_array(self, params, parent_name = None):
        i = 0
        for key in params:
            if key == 'pg_sig':
                continue
            
            name = parent_name + key + str(i)
            
            if type(params.get(key)) == dict:
                self.__make_flat_params_array(params, name)
                continue
            
            self.flat_array.update({key, params.get(key)})
            
        return self.flat_array            
    
    def __make_sig_str(self, script_name, params):
        params.pop('pg_sig', 'deleted')
        list_to_sort = list(params.keys());
        list_to_sort.sort()
        str_to_sig = script_name
        
        for key in list_to_sort:
            str_to_sig += params.get(key)
            
        str_to_sig += self.secret_key
        return str_to_sig
    
    def make(self, script_name, params):
        flat_params = self.__make_flat_params_array(params)
        return _md5.md5(self.__make_sig_str(script_name, flat_params))
                        
    def check(self, signature, script_name, xml):
        return signature == self.make_xml(script_name, xml)
    
    def make_xml(self, script_name, xml):
        flat_params = self.__make_flat_params_xml(xml)
        return self.make(script_name, flat_params)