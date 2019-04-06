from dinterpol import Template


# Template, input item, expected result
template_test_list = [
    ("", {}, ""),  # NOQA: W605
    ("Plain value", {}, "Plain value"),
    ("Plain value with \$ escaped", {}, "Plain value with $ escaped"),
    ("\$Plain value with escaped", {}, "$Plain value with escaped"),
    ("Plain value with escaped\$", {}, "Plain value with escaped$"),
    ("$num *2$", {"num": 3}, 6),
    ("Plain value with escaped\$", {}, "Plain value with escaped$"),
    ("Total=$num * 2$", {"num": 3}, "Total=6"),
    ({"Total": "$num*2$"}, {"num": 3}, {"Total": 6}),
    ({"Total": "$num+5$"}, {"num": 3}, {"Total": 8}),
    (["Zoom", "$num*2$"], {"num": 3}, ["Zoom", 6]),
    (["Zoom", "$num*2$"], {"num": 1}, ["Zoom", 2]),
    (["Zoom", "$ num*2 $"], {"num": 1}, ["Zoom", 2]),
    (["Zoom", "$ num*2 $"], {"num": 1}, ["Zoom", 2]),
    ("$a.b$", {"a": {"b": "c"}}, "c"),
]


def test_unbalanced():
    try:
        assert Template("This is $ not ok").substitute()
    except ValueError:
        pass
    else:
        raise Exception("Unbalanced $ test failed")


def test_template():
    for template, mapping, expected_result in template_test_list:
        print("Testing", template, mapping, expected_result)
        assert Template(template).render(mapping) == expected_result


def test_tag():
    template = "$_$$_tag['word']$"
    mapping = ""
    mapping_tag = {"word": "something"}
    assert Template(template).render(mapping, mapping_tag) == "something"
