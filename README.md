# dinterpol

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][travis-image]][travis-link]

---

dinterpol is a python library and a command line utility for data interpolation that supports both scalar and structured types generation.


## Motivation
When dealing with structured data types like dictionaries, or data formats like JSON and YAML it can be useful to generate scalar or structured types resulting from the interpolation of multiple input elements. Python3 provides several standard string interpolation mechanisms: [string.Template()], [f-strings] and [str.format()], but because they all return strings, they are not suitable for structured and non string data interpolation.


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
```

## Code of Conduct

Everyone interacting in the dinterpol project's codebase, issue trackers, chat
rooms, and mailing lists is expected to follow the [PyPA Code of Conduct].


[appveyor-image]: https://img.shields.io/appveyor/ci/d0ugal/mdatapipe/master.svg
[appveyor-link]: https://ci.appveyor.com/project/d0ugal/mdatapipe
[codecov-image]: http://codecov.io/github/mdatapipe/dinterpol/coverage.svg?branch=master
[codecov-link]: http://codecov.io/github/mdatapipe/dinterpol?branch=master
[landscape-image]: https://landscape.io/github/mdatapipe/dinterpol/master/landscape.svg?style=flat
[landscape-link]: https://landscape.io/github/mdatapipe/dinterpol/master
[pypi-v-image]: https://img.shields.io/pypi/v/dinterpol.svg
[pypi-v-link]: https://pypi.org/project/dinterpol/
[travis-image]: https://img.shields.io/travis/mdatapipe/dinterpol/master.svg
[travis-link]: https://travis-ci.org/mdatapipe/dinterpol

[dinterpol]: https://dinterpol.mdatapipe.org
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
