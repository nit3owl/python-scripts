def print_table(json):
    table_headers = ['Location', 'Date', 'AQI', 'Quality']
    for header in table_headers:
        print('{:^30}'.format(header), end='')
    
    print('\n' + '-' * (len(table_headers) * 30))

    for day in json:
        print('{:^30}{:^30}{:^30}{:^30}'.format(day['ReportingArea'][:30], day['DateForecast'], day['AQI'], day['Category']['Name']))

def fetch_report_by_zip(zipcode, api_key):
    base_url = 'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json'
    zip_param = 'zipCode={0}'.format(zipcode)
    date_param = 'date={0}'.format(datetime.datetime.today().strftime('%Y-%m-%d'))
    distance_param = 'distance={0}'.format(5)
    api_param = 'API_KEY={0}'.format(api_key)

    print(base_url + "&" + zip_param + "&" + date_param + "&" + distance_param + "&" + api_param + '\n')
    report = urllib.request.urlopen(base_url + "&" + zip_param + "&" + date_param + "&" + distance_param + "&" + api_param).read()
    parsed = json.loads(report.decode('utf8').replace("'", '"'))
    return parsed

def positive_five_digit_int(value):
    #this may not be a valid zipcode but zipcode validation is a pain
    i = int(value)
    if i < 0 or i > 99999:
        raise argparse.ArgumentTypeError('Invalid: Expected five digit zipcode, got {0}'.format(value))
    return i

def load_config():
    config_file = 'config.json'
    try:
        with open(config_file) as f:
            config = json.load(f)
    except FileNotFoundError:
        print('Script requires {0} file to run.'.format(config_file))
        sys.exit(1)
    
    return config

def get_api_key(config):
    api_key_keyword = 'api_key'
    try:
        api_key = config[api_key_keyword]
    except KeyError:
        print("Config requires an {0}.".format(api_key_keyword))
        sys.exit(1)

    return api_key
    

def main():
    parser = argparse.ArgumentParser(description = 'Fetch air quality reports because the websites are slow.')
    parser.add_argument('zipcode', type=positive_five_digit_int, help='Five digit zipcode')
    args = parser.parse_args()

    config = load_config()
    api_key = get_api_key(config)
    response = fetch_report_by_zip(args.zipcode, api_key)
    print_table(response)

import string
import datetime
import argparse
import urllib.request
import json
import sys

main()