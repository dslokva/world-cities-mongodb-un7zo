import os


def get_data_folder_path():
    current_folder = os.getcwd()
    return os.path.join(current_folder, 'data')


def get_country_data_path():
    return os.path.join(get_data_folder_path(), 'countryInfo.txt')


def get_city_data_path():
    return os.path.join(get_data_folder_path(), 'cities500.txt')


def get_alternate_names_data_path():
    return os.path.join(get_data_folder_path(), 'alternateNamesV2.txt')
