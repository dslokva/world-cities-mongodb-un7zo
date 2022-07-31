from utils.mongodb import init, save_cities, save_countries
from utils.parser import parse_city, parse_country, remove_non_match_language_countries_and_cities, parse_alternate_names

init()

parse_city()
parse_country()
parse_alternate_names()

remove_non_match_language_countries_and_cities()

save_cities()
save_countries()
