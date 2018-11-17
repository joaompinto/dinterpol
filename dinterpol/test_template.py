from dinterpol import Template

template_test_list = [  # NOQA: W605
    ("", {}, ""),   # NOQA: W605
    ("Plain value", {}, "Plain value"),
    ("Plain value with \$ escaped", {}, "Plain value with $ escaped"),
    ("\$Plain value with escaped", {}, "$Plain value with escaped"),
    ("Plain value with escaped\$", {}, "Plain value with escaped$"),
]


def test_unbalanced():
    try:
        assert(Template("This is $ not ok").substitute())
    except ValueError:
        pass
    else:
        raise Exception("Unbalanced $ test failed")


def test_template():
    for template, mapping, expected_result in template_test_list:
        assert(Template(template).substitute(mapping) == expected_result)
