"""
    catfacts.py
    ~~~~~~~~~~~

    Get and return facts from catfact.ninja

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""
import requests
import json

def get_joke():
	"""Returns a joke from the WebKnox one liner API."""


	page = requests.get("https://catfact.ninja/fact")
	joke = json.loads(page.content.decode("UTF-8"))

	return joke["fact"]
