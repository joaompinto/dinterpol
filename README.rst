dinterpol
=========

|PyPI Version| |Build Status|

--------------

dinterpol is a python library and a command line utility for data
interpolation that supports both scalar and structured types generation.

Motivation
----------

When dealing with structured data types like dictionaries, or data
formats like JSON and YAML it can be useful to generate scalar or
structured types resulting from the interpolation of multiple input
elements. Python3 provides several standard string interpolation
mechanisms:
`string.Template() <https://docs.python.org/3/library/string.html#string.Template>`__,
`f-strings <https://docs.python.org/3/reference/lexical_analysis.html#f-strings>`__
and
`str.format() <https://docs.python.org/3/library/stdtypes.html#str.format>`__,
but because they all return strings, they are not suitable for
structured and non string data interpolation.

Usage example:

.. code:: python

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

Code of Conduct
---------------

Everyone interacting in the dinterpol project's codebase, issue
trackers, chat rooms, and mailing lists is expected to follow the `PyPA
Code of Conduct <https://www.pypa.io/en/latest/code-of-conduct/>`__.

.. |PyPI Version| image:: https://img.shields.io/pypi/v/dinterpol.svg
   :target: https://pypi.org/project/dinterpol/
.. |Build Status| image:: https://img.shields.io/travis/mdatapipe/dinterpol/master.svg
   :target: https://travis-ci.org/mdatapipe/dinterpol
