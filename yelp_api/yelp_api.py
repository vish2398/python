import requests
import json
import configparser

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

config = configparser.ConfigParser()
config.read("/usr/local/etc/python_config.txt")

API_HOST = "https://api.yelp.com"
SEARCH_PATH = "/v3/businesses/search"
SEARCH_LIMIT = 3
API_KEY = config.get("YELP_API", "apikey")


def request(host, path, api_key, url_params=None):
	url_params = url_params or {}
	url ='{0}{1}'.format(host, quote(path.encode('utf8')))
	headers = {
		'Authorization' : 'Bearer %s' % api_key,
	}

	print(u'Querying {0} ...'.format(url))

	response = requests.request('GET', url, headers=headers, params=url_params)

	print(response.json())
	return response.json()


def search(term, location):
	url_params = {
		'term': term.replace(' ', '+'),
		'location': location.replace(' ', '+'),
		'limit': SEARCH_LIMIT
	}
	return request(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params)

def main():
	try:
		search("pizza", "New York City")
	except:
		sys.exit(
        'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
            error.code,
            error.url,
            error.read(),
        	)
    	)

if __name__ == '__main__':
    main()