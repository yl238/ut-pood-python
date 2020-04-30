class BottleVerse:
    @classmethod
    def lyrics(cls, number):
        return cls(BottleNumber.for_number(number)).my_lyrics()
        
    def __init__(self, bottle_number):
        self.bottle_number = bottle_number
    
    def my_lyrics(self):
        return f"{self.bottle_number} of beer on the wall, ".capitalize() + \
        f"{self.bottle_number} of beer.\n" + \
        f"{self.bottle_number.action()}, " + \
        f"{self.bottle_number.successor()} of beer on the wall.\n"

class CountdownSong:
    def __init__(self, verse_template=BottleVerse, _max=99, _min=0):
        self.verse_template = verse_template
        self._max = _max
        self._min = _min

    def song(self):
        return self.verses(self._max, self._min)

    def verses(self, _max, _min):
        return '\n'.join(map(self.verse, range(_max, _min-1, -1)))

    def verse(self, number):
        return self.verse_template(number).lyrics(number)
        
# Demeter violation
# remove constants
# detail with instances instead of classes
class BottleNumber:
    def __init__(self, number):
        self.number = number

    @classmethod
    def for_number(cls, number):
        if number == 0:
            return BottleNumber0(number)
        elif number == 1:
            return BottleNumber1(number)
        else:
            return cls(number)

    def quantity(self):
        return self.number

    def container(self):
        return "bottles"

    def action(self):
        return f"Take {self.pronoun()} down and pass it around"
    
    def pronoun(self):
        return 'one'
    
    def successor(self):
        return BottleNumber.for_number(self.number - 1)

    def __repr__(self):
        return f"{self.quantity()} {self.container()}"


class BottleNumber0(BottleNumber):
    def quantity(self):
        return "no more"

    def action(self):
        return "Go to the store and buy some more"

    def successor(self):
        return BottleNumber.for_number(99)


class BottleNumber1(BottleNumber):
    def container(self):
        return 'bottle'
    
    def pronoun(self):
        return "it"