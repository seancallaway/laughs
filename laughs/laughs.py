"""
    laughs.py
    ~~~~~~~~~

    Functions that return jokes.

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""
from random import randint
from .services import ronswanson, chucknorris, catfacts, dadjokes

NUM_SERVICES = 4


def get_joke():
	"""Return a jokes from one of the random services."""
	service_num = randint(1, NUM_SERVICES)
	return load_joke(service_num)


def load_joke(service_num=1):
	"""Pulls the joke from the service based on the argument."""
	result = {
	  1 : ronswanson.get_joke(),
	  2 : chucknorris.get_joke(),
	  3 : catfacts.get_joke(),
	  4 : dadjokes.get_joke(),
	}.get(service_num)

	return result
