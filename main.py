from utils.mongodb import init, save_cities, save_countries, save_dxcc
from utils.parser import parse_city, parse_country, remove_non_match_language_countries_and_cities, parse_alternate_names, parse_dxcc

init()

parse_city()
parse_country()
parse_alternate_names()
parse_dxcc()

remove_non_match_language_countries_and_cities()

save_cities()
save_countries()
save_dxcc()