import re
import json
import requests

BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
# deal with data coming from CSSE that doesn't match known Country names or ISO country code. 
COUNTRY_MAPPING = {
    "US": "United States",
    "Congo (Brazzaville)": "Republic of the Congo",
    "Congo (Kinshasa)": "Democratic Republic of the Congo",
    "Cote d'Ivoire": "Ivory Coast",
    "Korea, South": "South Korea",
    "Korea, North": "North Korea",
    "Taiwan*": "Taiwan",
}

def get_daily_report(period):
    """Get covid-19 daily reports and transform the .csv file into a python dict. 
    
    Keyword arguments:
    period: a string representing the current date (using format: mm-dd-yyyy, e.g 03-22-2020),

    Returns: json
    """
    try:
        url = f'{BASE_URL}/{period}.csv' 
        response = {}  # will hold the final dataset

        r = requests.get(url)

        if r.status_code == 200:
            # load json country_code
            with open('app/country_code.json') as f:
                country_codes = json.load(f)
            
            dataset = [e for e in r.text.split('\n')[1:]] # gets rid of .cvs header, and transform dataset
            
            for el in dataset:
                data = re.split(',(?!\s)', el) # to deal with countries that have 'double name' i.e "Korea, South"
                
                if data and data != ['']:
                    country_name = data[3].replace('"', '')
                    # clean CSSE data to confirm to/with ISO standards.
                    if country_name in COUNTRY_MAPPING:
                        country_name = COUNTRY_MAPPING[country_name]
                    
                    country_code = get_country_code(country_name, country_codes)
                    
                    if country_code is not None:
                        if country_code in response:
                            response[country_code].append( {'province': data[2], 'confirmed': data[7], \
                                    'deaths': data[8], 'recovered': data[9]} )
                        else:
                            response[country_code] = [ {'province': data[2], 'confirmed': data[7], \
                                    'deaths': data[8], 'recovered': data[9]} ]
        return json.dumps(response, sort_keys=True)
    except requests.ConnectionError as e:
        # TODO: handle error
        pass

def get_country_code(name, country_codes):
    alpha_2_code = None  # alpha2 is made up of 2 letters.
    for key, value in country_codes.items():
        if value == name:
            alpha_2_code = key
    return alpha_2_code
