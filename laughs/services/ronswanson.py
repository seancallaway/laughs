"""
    ronswanson.py
    ~~~~~~~~~~~~~

    Get and return jokes from ron-swanson-quotes

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""
import requests
import json

def get_joke():
	"""Return a Ron Swanson quote."""

	page = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes")
	jokes = []
	jokes = json.loads(page.content.decode(page.encoding))

	return '"' + jokes[0] + '" - Ron Swanson'
