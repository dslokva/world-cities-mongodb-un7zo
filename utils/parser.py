import csv
import re
import settings
from datetime import datetime
from utils.paths import get_city500_data_path, get_country_data_path, get_alternate_names_data_path, get_dxcc_data_path, get_lotw_file_path
from models.AlternateName import AlternateName
from models.City import City
from models.Dxcc import Dxcc
from models.Country import Country
from models.LotwUserActivity import LotwUserActivity


def read_csv_by_line(file_path, callback, dialect='excel-tab'):
    with open(file_path, encoding="utf8") as file_to_parse:
        for line in csv.reader(file_to_parse, dialect):
            if line and not line[0].startswith("#"):
                callback(line)


#########################
#   Parse the cities    #
#########################
cities = []
cities_dict = {}
dxcc_data = []
lotw_useractivity_data = []


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def filter_cyrillic(names_list):
    for name in names_list:
        if has_cyrillic(name):
            return name


def save_extra_city_fields(city):
    def get_attrs_to_add():
        attrs_to_add = {
            'city_id': getattr(city, 'city_id')
        }
        for attr in settings.CITY_FIELDS_TO_ADD:
            attrs_to_add[attr] = getattr(city, attr)

        if settings.ADD_CITY_CYRILLIC_NAME_TO_COUNTRY:
            attrs_to_add['name_ru'] = filter_cyrillic(getattr(city, 'alternate_names'))

        return attrs_to_add

    if not settings.ADD_CITY_TO_COUNTRY:
        return

    if not city.country_code in cities_dict:
        cities_dict[city.country_code] = []

    cities_dict[city.country_code].append(get_attrs_to_add())


def parse_city_callback(line):
    city = City(line)
    cities.append(city.to_dict())
    save_extra_city_fields(city)


def parse_dxcc_callback(line):
    dxcc = Dxcc(line)
    dxcc_data.append(dxcc.to_dict())


def parse_lotw_callback(line):
    lotw = LotwUserActivity(line)
    combined_dict = {}
    combined_dict['callsign'] = lotw.callsign
    combined_dict['datetime'] = datetime.strptime(lotw.activity_date + ' ' + lotw.activity_time, '%Y-%m-%d %H:%M:%S')
    # 2008-09-16,17:36:57
    lotw_useractivity_data.append(combined_dict)


def parse_altername_name_callback(line):
    alternate_name = AlternateName(line)

    if alternate_name.is_historical:
        return
    if not alternate_name.alter_name_type:
        return
    if not int(alternate_name.real_item_id) in countries_ids:
        return
    
    if alternate_name.alter_name_type == 'ru':
        for country in countries:
            if country['country_id'] == int(alternate_name.real_item_id):
                country['country_ru'] = alternate_name.alter_name


def parse_alternate_names():
    if settings.ADD_COUNTRY_CYRYLLIC_NAME:
        read_csv_by_line(get_alternate_names_data_path(), parse_altername_name_callback)


def parse_city():
    read_csv_by_line(get_city500_data_path(), parse_city_callback)


def parse_dxcc():
    read_csv_by_line(get_dxcc_data_path(), parse_dxcc_callback)


def clue_lotwuser_datetime(lotw_file_path):
    pass


def parse_lotw():
    with open(get_lotw_file_path(), newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
    read_csv_by_line(get_lotw_file_path(), parse_lotw_callback, dialect)


#########################
#  Parse the countries  #
#########################
countries = []
countries_ids = []
countries_dict = {}
match_language_countries_iso = []


def parse_country_callback(line):
    country = Country(line)
    countries.append(country.to_dict())
    countries_ids.append(country.country_id)
    if settings.ADD_COUNTRY_TO_CITY:
        countries_dict[country.iso] = country

    if settings.ONLY_LANGUAGE:
        for language in country.languages:
            if language in settings.ONLY_LANGUAGE:
                match_language_countries_iso.append(country.iso)
                break


def parse_country():
    read_csv_by_line(get_country_data_path(), parse_country_callback)


# Extra filter:
# To only add the countries and cities which use language in settings.ONLY_LANGUAGE
# We can filter the contries when processing to gain more performance
# But I like to keep they all here to cleaner logic.
def remove_non_match_language_countries_and_cities():
    if not settings.ONLY_LANGUAGE:
        return

    cities[:] = [c for c in cities if c['country_code'] in match_language_countries_iso]
    countries[:] = [c for c in countries if c['iso'] in match_language_countries_iso]
