import sys
sys.path.append('.')
import unittest
from pybottles.lib.bottles import CountdownSong, BottleVerse

class TestBottleVerse(unittest.TestCase):
    def test_the_first_verse(self):
        expected = "99 bottles of beer on the wall, " + \
        "99 bottles of beer.\n" + \
        "Take one down and pass it around, " + \
        "98 bottles of beer on the wall.\n"
        self.assertEqual(expected, BottleVerse.lyrics(99))

    def test_another_verse(self):
        expected = "3 bottles of beer on the wall, " + \
        "3 bottles of beer.\n" + \
        "Take one down and pass it around, " + \
        "2 bottles of beer on the wall.\n"
        self.assertEqual(expected, BottleVerse.lyrics(3))

    def test_verse_2(self):
        expected = "2 bottles of beer on the wall, " + \
        "2 bottles of beer.\n" + \
        "Take one down and pass it around, " + \
        "1 bottle of beer on the wall.\n"
        self.assertEqual(expected, BottleVerse.lyrics(2))

    def test_verse_1(self):
        expected = "1 bottle of beer on the wall, " + \
        "1 bottle of beer.\n" + \
        "Take it down and pass it around, " + \
        "no more bottles of beer on the wall.\n" 
        self.assertEqual(expected, BottleVerse.lyrics(1))

    def test_verse_0(self):
        expected = "No more bottles of beer on the wall, " \
        "no more bottles of beer.\n" \
        "Go to the store and buy some more, " \
        "99 bottles of beer on the wall.\n" 
        self.assertEqual(expected, BottleVerse.lyrics(0))
    

class VerseFake:
    def __init__(self, number):
        self.number = number
    @classmethod
    def lyrics(cls, number):
        return f"This is verse {number}.\n"

class VerseFakeTest(unittest.TestCase):
    pass

class TestCountdownSong(unittest.TestCase):  
    
    def test_verse(self):
        expected = "This is verse 500.\n"
        self.assertEqual(expected, CountdownSong(verse_template=VerseFake).verse(500))

    def test_verses(self):
        expected = "This is verse 99.\n" \
        "\n" \
        "This is verse 98.\n" \
        "\n" \
        "This is verse 97.\n"
        self.assertEqual(expected, CountdownSong(
            verse_template=VerseFake).verses(99, 97))

    def test_song(self):
        expected = "This is verse 47.\n" \
        "\n" \
        "This is verse 46.\n" \
        "\n" \
        "This is verse 45.\n" \
        "\n" \
        "This is verse 44.\n" \
        "\n" \
        "This is verse 43.\n"
        self.assertEqual(expected, CountdownSong(
            verse_template=VerseFake, _max=47, _min=43).song())

if __name__ == '__main__':
    unittest.main()