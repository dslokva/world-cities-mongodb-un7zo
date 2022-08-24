DXCC_FIELDS = {
    'dxcc_id': 0, # integer id of record in dxcc database
    'name': 1  # name of geographical point (utf8)
}

class Dxcc(object):
    def __init__(self, data):
        super(Dxcc, self).__init__()

        if not isinstance(data, list):
            raise ValueError("Expect data to be a list")

        self.dxcc_id = int(data[DXCC_FIELDS['dxcc_id']])
        self.name = data[DXCC_FIELDS['name']]


    def to_dict(self):
        return  self.__dict__
