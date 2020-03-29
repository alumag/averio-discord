import urllib3
import requests
from base64 import b64decode

from product import Product

READ_MODE = "r"
ENCODING = "utf-8"

AVERIO_URL = "https://elk.averio.de/avp-diff/_msearch"
QUERY_SIZE = 30
REQUEST_TIMEOUT = 30

# averio post request headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko'
                  '/20100101 Firefox/61.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://averio.de/deals',
    'content-type': 'application/x-ndjson',
}

# averio post request data
with open("averio_query_data.json", READ_MODE, encoding=ENCODING) as fd:
    query_data_raw = fd.read().replace('QUERY_SIZE', str(QUERY_SIZE))

urllib3.disable_warnings()


def request_products():
    """
    Request for all the current products on averio website.
    :return: averio responses, JSON
    :rtype: C{list}
    """

    try:
        response = requests.post(AVERIO_URL, headers=headers,
                                 data=query_data_raw, verify=False,
                                 timeout=REQUEST_TIMEOUT)
    except (ConnectionError, TimeoutError) as e:
        print("Connection error, check the connection of either your machine"
              " and averio site.")
        raise e
    except requests.HTTPError as e:
        print("HTTPError occurred, Check for errors on averion site.")
        raise e
    else:
        return response.json()['responses']


def parse_hit_products(averio_responses):
    """
    Parse averio search query into hits.
    :return: Products
    :rtype: C{set} of Product instances.
    """
    products_lists = set()
    for response in averio_responses:
        for hit in response['hits']['hits']:
            products_lists.add(
                Product(product=hit['_source']['product'],
                        link=b64decode(hit['_source']['key_id']).
                        decode(ENCODING),
                        old_price=hit['_source']['old_price'],
                        new_price=hit['_source']['new_price'],
                        percent=hit['_source']['percent'])
            )
    return products_lists


def get_new_products():
    """
    Yield the new products on every call
    """
    last_products = set()
    while True:
        responses = request_products()
        products = parse_hit_products(responses)
        # Yield the new products only (depends on product name)
        yield products.difference(last_products)
        last_products.update(products)
