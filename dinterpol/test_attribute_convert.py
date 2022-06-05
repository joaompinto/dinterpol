from datetime import datetime
from . import Template


def test_disable_attribute_convert():
    Template({"today is": "{now.day}"}, False).render({"now": datetime.now()})
