
CITY_ALTER_NAMES_FIELDS = {
    'alter_name_id': 0, # integer id of record in geonames database
    'real_item_id': 1, #
    'alter_name_type': 2, # --- The language code is refering to the ISO-639-2 and ISO-639-3 codes, like:
                          # en (english), fr (french), ...
                          # ---or--- Accepted pseudo language codes:
                          # post (postal codes)
                          # icao, iata, faac, tcid (airport codes)
                          # abbr (abbreviation)
                          # link (link to website)
                          # phon (phonetics)
                          # piny (pinyin)
                          # wkdt (wikidataid)
                          # unlc (UNLOCODE)
    'city_name': 3, # name of geographical point in plain ascii characters, varchar(200)
    'is_preferred': 4,
    'is_short': 5,
    'is_colloquial': 6,
    'is_historical': 7,
    'from_year': 8,
    'to_year': 9
}


class AlternateName(object):
    def __init__(self, data):
        super(AlternateName, self).__init__()

        if not isinstance(data, list):
            raise ValueError("Expect data to be a list")

        self.alter_name_id = int(data[CITY_ALTER_NAMES_FIELDS['alter_name_id']])
        self.real_item_id = data[CITY_ALTER_NAMES_FIELDS['real_item_id']]
        self.alter_name_type = data[CITY_ALTER_NAMES_FIELDS['alter_name_type']]
        self.alter_name = data[CITY_ALTER_NAMES_FIELDS['city_name']]
        self.is_preferred = data[CITY_ALTER_NAMES_FIELDS['is_preferred']]
        self.is_short = data[CITY_ALTER_NAMES_FIELDS['is_short']]
        self.is_historical = data[CITY_ALTER_NAMES_FIELDS['is_historical']]
        self.is_colloquial = data[CITY_ALTER_NAMES_FIELDS['is_colloquial']]
        self.from_year = data[CITY_ALTER_NAMES_FIELDS['from_year']]
        self.to_year = data[CITY_ALTER_NAMES_FIELDS['to_year']]
