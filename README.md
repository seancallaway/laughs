# laughs
> A python package that pulls jokes from various APIs.

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][pypi-downloads]][pypi-url]
[![Release Status][release-status]][pypi-url]

laughs provides a python package for generating pulling jokes from various unauthenticated
APIs around the Internet. Jokes are provided by the `get_joke()` function. The package works 
with python 2 and 3.

Pull requests are welcome!

## Installation

OS X & Linux:

```sh
pip install laughs
```

or

```sh
pip3 install laughs
```

Windows:

```sh
python3 -m pip install laughs
```

## Development setup

Using laughs in your projects:
```python
import laughs
joke = laughs.get_joke() # returns a string containing a joke/quote
```

## Release History
* 0.1.0
    * The first proper release

## Meta

Sean Callaway – [@smcallaway](https://twitter.com/smcallaway) – seancallaway@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/seancallaway/laughs](https://github.com/seancallaway/laughs)

## Contributing

1. Fork it (<https://github.com/seancallaway/laughs/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[pypi-image]: https://img.shields.io/pypi/v/laughs.svg
[pypi-url]: https://pypi.python.org/pypi/laughs
[travis-image]: https://api.travis-ci.org/seancallaway/laughs.svg?branch=master
[travis-url]: https://travis-ci.org/seancallaway/laughs
[pypi-downloads]: https://img.shields.io/pypi/dm/laughs.svg
[release-status]: https://img.shields.io/pypi/status/laughs.svg
