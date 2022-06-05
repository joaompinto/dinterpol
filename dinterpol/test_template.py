from . import Template


# Template, input item, expected result
template_test_list = [
    ("", {}, ""),  # NOQA: W605
    ("Plain value", {}, "Plain value"),
    (r"Plain value with \{ escaped", {}, "Plain value with { escaped"),
    (r"\{Plain value with escaped", {}, "{Plain value with escaped"),
    (r"Plain value with escaped\}", {}, "Plain value with escaped}"),
    ("{num * 2}", {"num": 3}, 6),
    ("Total={num * 2}", {"num": 3}, "Total=6"),
    ({"Total": "{num*2}"}, {"num": 3}, {"Total": 6}),
    ({"Total": "{num+5}"}, {"num": 3}, {"Total": 8}),
    ("{a.b}", {"a": {"b": "c"}}, "c"),
    (["this", "{num}"], {"num": 3}, ['this', 3]),
]


def test_unbalanced():
    try:
        assert Template("This is { not ok").render({})
    except ValueError:
        pass


def test_template():
    for template, mapping, expected_result in template_test_list:
        assert Template(template).render(mapping) == expected_result
