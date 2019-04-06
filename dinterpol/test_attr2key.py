from .attr2key import attr2key


def test_attr2key():
    test_data = {"a": 12, "b": {"a": "good", "b": "bad"}}  # NOQA: F841

    # Test simple replacement
    assert eval(attr2key("test_data['a']")) == 12
    assert eval(attr2key("test_data.a")) == 12
    assert eval(attr2key("test_data.a + 1")) == 13
    assert eval(attr2key("test_data.a + 1")) == 13

    # Test mixed replacement with functions
    assert eval(attr2key("test_data['b'].a.upper()")) == "GOOD"
    assert eval(attr2key("test_data.b.a.upper()")) == "GOOD"
