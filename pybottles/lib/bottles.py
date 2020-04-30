class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(map(self.verse, range(upper, lower-1, -1)))

    def verse(self, number):
        bottle_number = self.bottle_number_for(number)
        next_bottle_number = self.bottle_number_for(bottle_number.successor)

        return f"{bottle_number} of beer on the wall, ".capitalize() + \
        f"{bottle_number} of beer.\n" + \
        f"{bottle_number.action}, " + \
        f"{next_bottle_number} of beer on the wall.\n"

    def bottle_number_for(self, number):
        if number == 0:
            return BottleNumber0(number)
        elif number == 1:
            return BottleNumber1(number)
        else:
            return BottleNumber(number) 

class BottleNumber:
    def __init__(self, number):
        self.number = number
        self.quantity = self.set_quantity()
        self.container = self.set_container()
        self.action = self.set_action()
        self.pronoun = self.set_pronoun()
        self.successor = self.set_successor()

    def __repr__(self):
        return f"{self.quantity} {self.container}"

    def set_quantity(self):
        return str(self.number)

    def set_container(self):
        return "bottles"

    def set_action(self):
        return f"Take {self.set_pronoun()} down and pass it around"
    
    def set_pronoun(self):
        return 'one'
    
    def set_successor(self):
        return self.number - 1


class BottleNumber0(BottleNumber):
    def set_quantity(self):
        return "no more"

    def set_action(self):
        return "Go to the store and buy some more"

    def set_successor(self):
        return 99

class BottleNumber1(BottleNumber):
    def set_container(self):
        return 'bottle'
    
    def set_pronoun(self):
        return "it"



if __name__ == '__main__':
    bottle = Bottles()
    print(bottle.song())