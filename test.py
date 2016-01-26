from collections import OrderedDict
from unittest import TestCase
from converter import Converter
from utils import conv_dict_to_odict


class OKTestCase(TestCase):
    def test_(self):
        d = OrderedDict((
            ("A",
                OrderedDict((("1", 'o'), ("2", 'o'), ("3", 'x'),))),
            ("B",
                OrderedDict((("1", 'x'), ("3", 'o'),))),
            ("D",
                OrderedDict((("1", 'x'), ("2", 'x'), ("3", 'x'),))),
            ("E",
                OrderedDict(
                    (("1", 'x'), ("2", 'x'), ("3", 'x'), ("5", "x"),))),
            ("F", OrderedDict()),))

        converter = Converter()
        csv_data = converter.convert(d)

        header = csv_data.readline()
        self.assertEqual(header, ",1,2,3,5\n")
        a = csv_data.readline()
        self.assertEqual(a, "A,o,o,x,\n")
        b = csv_data.readline()
        self.assertEqual(b, "B,x,,o,\n")
        d = csv_data.readline()
        self.assertEqual(d, "D,x,x,x,\n")
        e = csv_data.readline()
        self.assertEqual(e, "E,x,x,x,x\n")
        f = csv_data.readline()
        self.assertEqual(f, "F,,,,\n")

    def test_conv_dict_to_odict(self):
        d = {
            "a": {
                '1': 'x'
            },
            "b": {
                "1": 'x', "2": 'o'
            },
            "c": {
            },
            "d": {
                "5": 'x'
            }
        }
        odict_d = conv_dict_to_odict(d)
        assert_d = OrderedDict(
            (
                ("a", OrderedDict((('1', 'x'),))),
                ("b", OrderedDict((('1', 'x'), ('2', 'o')))),
                ("c", OrderedDict()),
                ("d", OrderedDict((('5', 'x'),))),
            ),
        )
        self.assertDictEqual(odict_d, assert_d)
