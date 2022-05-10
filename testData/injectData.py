import json
from collections import OrderedDict, namedtuple

class injectData():
    def create_namedtuple_from_dict(obj):
        """converts given list or dict to named tuples, generic alternative to dataclass"""
        if isinstance(obj, dict):
            fields = sorted(obj.keys())
            namedtuple_type = namedtuple(
                typename='TestData',
                field_names=fields,
                rename=True,
            )
            field_value_pairs = OrderedDict(
                (str(field), injectData.create_namedtuple_from_dict(obj[field]))
                for field in fields
            )
            try:
                return namedtuple_type(**field_value_pairs)
            except TypeError:
                # Cannot create namedtuple instance so fallback to dict (invalid attribute names)
                return dict(**field_value_pairs)
        elif isinstance(obj, (list, set, tuple, frozenset)):
            return [injectData.create_namedtuple_from_dict(item) for item in obj]
        else:
            return obj

    def inject_test_data(TESTDATA_PATH):
        with open(TESTDATA_PATH) as data_file:
            test_data = json.load(data_file)
        return injectData.create_namedtuple_from_dict(test_data)
