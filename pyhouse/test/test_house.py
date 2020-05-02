import unittest
from pyhouse.lib.house import CumulativeTale


class CumulativeTaleTest(unittest.TestCase):
    def setUp(self):
        self.tale = CumulativeTale()

    def test_line_1(self):
        expected = "This is the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(1))

    def test_line_2(self):
        expected = "This is the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(2))

    def test_line_3(self):
        expected = "This is the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(3))

    def test_line_4(self):
        expected = "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(4))
    
    def test_line_5(self):
        expected = "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(5))

    def test_line_6(self):
        expected = "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(6))

    def test_line_7(self):
        expected = "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(7))

    def test_line_8(self):
        expected = "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(8))
  
    def test_line_9(self):
        expected = "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(9))
  
    def test_line_10(self):
        expected = "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(10))
  
    def test_line_11(self):  
        expected = "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(11))
  
    def test_line_12(self):
        expected = "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.\n"
        self.assertEqual(expected, self.tale.line(12))

    def test_all_the_lines(self):
        expected = """This is the house that Jack built.

This is the malt that lay in the house that Jack built.

This is the rat that ate the malt that lay in the house that Jack built.

This is the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.

This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.
"""
        self.assertEqual(expected, self.tale.recite())
if __name__ == '__main__':
    unittest.main()