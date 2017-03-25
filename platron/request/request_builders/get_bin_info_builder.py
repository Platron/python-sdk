from platron.request.request_builders.request_builder import RequestBuilder

class GetBinInfoBuilder(RequestBuilder):
    '''
    Get bin info API request
    '''


    def __init__(self, card_bin):
        self.pg_bin = card_bin
       
    def get_url(self):
        return self.PLATRON_URL + 'get_bin_info.php'