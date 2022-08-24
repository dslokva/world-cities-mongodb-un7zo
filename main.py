from utils.mongodb import init, save_cities, save_countries, save_dxcc, save_lotw
from utils.parser import *

init()

# parse_city()
# parse_country()
# parse_alternate_names()
# parse_dxcc()
parse_lotw()

# remove_non_match_language_countries_and_cities()

# save_cities()
# save_countries()
# save_dxcc()
save_lotw()