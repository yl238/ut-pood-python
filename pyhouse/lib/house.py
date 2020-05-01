import random

class RandomOrderer(object):
    def order(self, data):
        random.shuffle(data)
        return data

class OriginalOrderer(object):
    def order(self, data):
        return data


class PiratePrefixer(object):
    def prefix(self):
        return 'Thar be'

class MundanePrefixer(object):
    def prefix(self):
        return 'This is'

class House(object):
    DATA = ["the horse and the hound and the horn that belonged to",
      "the farmer sowing his corn that kept",
      "the rooster that crowed in the morn that woke",
      "the priest all shaven and shorn that married",
      "the man all tattered and torn that kissed",
      "the maiden all forlorn that milked",
      "the cow with the crumpled horn that tossed",
      "the dog that worried",
      "the cat that killed",
      "the rat that ate",
      "the malt that lay in",
      "the house that Jack built"]

    def __init__(self, orderer=OriginalOrderer(), prefixer=MundanePrefixer()):
        self.data = orderer.order(self.DATA)
        self.prefix = prefixer.prefix()

    def recite(self):
        return '\n'.join([self.line(i) for i in range(1, 13)])

    def phrase(self, number):
        return " ".join(self.data[-number:])


    def line(self, number):
        return f"{self.prefix} {self.phrase(number)}.\n"


if __name__ == '__main__':
    print(House(orderer=RandomOrderer()).line(12))
    print(House(prefixer=PiratePrefixer()).line(12))
    print(House(prefixer=PiratePrefixer(), orderer=RandomOrderer()).line(12))    