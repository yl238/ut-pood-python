class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(map(self.verse, range(upper, lower-1, -1)))

    def verse(self, number):
        bottle_number = BottleNumber.for_number(number)
       
        return f"{bottle_number} of beer on the wall, ".capitalize() + \
        f"{bottle_number} of beer.\n" + \
        f"{bottle_number.action()}, " + \
        f"{bottle_number.successor()} of beer on the wall.\n"


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


if __name__ == '__main__':
    bottle = Bottles()
    print(bottle.verses(2, 1))