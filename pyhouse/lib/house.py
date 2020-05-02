import random

HOUSE_DATA = [
    ["the horse and the hound and the horn", "", "that belonged to"],
    ["the farmer", "sowing his corn", "that kept"],
    ["the rooster", "that crowed in the morn", "that woke"],
    ["the priest", "all shaven and shorn",  "that married"],
    ["the man", "all tattered and torn",  "that kissed"],
    ["the maiden", "all forlorn", "that milked"],
    ["the cow with the crumpled horn", "that tossed"],
    ["the dog", "", "that worried"],
    ["the cat", "", "that killed"],
    ["the rat", "", "that ate"],
    ["the malt", "", "that lay in"],
    ["the house", "", "that Jack built"]
]


class RandomOrderer(object):
    def order(self, data):
        random.shuffle(data)
        return data
    

class OriginalOrderer(object):
    def order(self, data):
        return data


class RandomButLastOrderer(object):
    def order(self, data):
        random.shuffle(data[:-1])
        return data


class MixedColumnOrderer(object):
    def order(self, data):
        for el in data: random.shuffle(el)
        return data


class PiratePrefixer(object):
    def prefix(self):
        return 'Thar be'


class MundanePrefixer(object):
    def prefix(self):
        return 'This is'


class Phrases(object):
    def __init__(self, orderer=OriginalOrderer(), input_data=HOUSE_DATA):
        self.data = orderer.order(input_data)

    def phrase(self, num):
        flatten = [item for sublist in self.data[-num:] for item in sublist]
        return ' '.join(' '.join(flatten).split())
        
    def size(self):
        return len(self.data)


class CumulativeTale(object):
    def __init__(self, phrases=Phrases(), prefixer=MundanePrefixer()):
        self.phrases = phrases
        self.prefix = prefixer.prefix()

    def recite(self):
        return '\n'.join([self.line(i) for i in range(1, 13)])

    def phrase(self, number):
        return self.phrases.phrase(number)

    def line(self, number):
        return f"{self.prefix} {self.phrase(number)}.\n"


if __name__ == '__main__':
    print(CumulativeTale(phrases=Phrases(orderer=MixedColumnOrderer())).line(12))
