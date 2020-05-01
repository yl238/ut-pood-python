import random

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

    def data(self):
        return self.DATA

    def recite(self):
        return '\n'.join([self.line(i) for i in range(1, 13)])

    def phrase(self, number):
        return " ".join(self.data()[-number:])

    def prefix(self):
        return "This is"

    def line(self, number):
        return f"{self.prefix()} {self.phrase(number)}.\n"


# This is a little ugly, but shuffle works in-place
class RandomHouse(House):
    def data(self):
        random.shuffle(super(RandomHouse, self).data())
        return super(RandomHouse, self).data()


class PirateHouse(House):
    def prefix(self):
        return "Thar be"


if __name__ == '__main__':
    print(PirateHouse().line(12))

    