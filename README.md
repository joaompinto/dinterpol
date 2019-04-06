# dinterpol

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
---

dinterpol is a python library for data interpolation that supports both scalar and structured types generation.


## Motivation
When dealing with structured data types like dictionaries, or data formats like JSON and YAML it can be useful to generate scalar or structured types resulting from the interpolation of multiple input elements. Python3 provides several standard string interpolation mechanisms: [string.Template()], [f-strings] and [str.format()], but because they all return strings, they are not suitable for structured with non string data interpolation.


[string.Template()]: https://docs.python.org/3/library/string.html#string.Template
[f-strings]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
[str.format()]: https://docs.python.org/3/library/stdtypes.html#str.format

Usage example:

```python
from dinterpol import Template

data = {
    "product": "pie",
    "quantity": 33,
    "price": 14,
    "details": { "size": 10, "flavour": "orange"}
}

# simple key interpolation for string generation
Template("We have $quantity$ $product$(s)").render(data)
'We have 33 pie(s)'

# python expression for string generation, expression result concatnated with string
Template("Total price is $quantity * price$").render(data)
'Total price is 426'

# python expression for dict generation, type inferred directly from expression's eval()
Template({ "total": "$quantity * price$"}).render(data)
{'total': 426}

# Use attribute style references for key access
Template("$details.size$").render(data)
10

```


## Code of Conduct

Everyone interacting in the dinterpol project's codebase, issue trackers, chat
rooms, and mailing lists is expected to follow the [PyPA Code of Conduct].


[appveyor-image]: https://img.shields.io/appveyor/ci/d0ugal/Openpipe/master.svg
[appveyor-link]: https://ci.appveyor.com/project/d0ugal/Openpipe
[codecov-image]: http://codecov.io/github/Openpipe/dinterpol/coverage.svg?branch=master
[codecov-link]: http://codecov.io/github/Openpipe/dinterpol?branch=master
[landscape-image]: https://landscape.io/github/Openpipe/dinterpol/master/landscape.svg?style=flat
[landscape-link]: https://landscape.io/github/Openpipe/dinterpol/master
[pypi-v-image]: https://img.shields.io/pypi/v/dinterpol.svg
[pypi-v-link]: https://pypi.org/project/dinterpol/
[travis-image]: https://img.shields.io/travis/Openpipe/dinterpol/master.svg
[travis-link]: https://travis-ci.org/Openpipe/dinterpol

[dinterpol]: https://dinterpol.Openpipe.org
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
