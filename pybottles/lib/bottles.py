class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join(map(self.verse, range(upper, lower-1, -1)))

    def verse(self, number):
        bottle_number = BottleNumber(number)
        next_bottle_number = BottleNumber(bottle_number.successor)

        return f"{bottle_number.quantity.capitalize()} {bottle_number.container} of beer on the wall, " \
        f"{bottle_number.quantity} {bottle_number.container} of beer.\n"\
        f"{bottle_number.action}, "\
        f"{next_bottle_number.quantity} {next_bottle_number.container} of beer on the wall.\n"

    def amount(self, number):
        if number == 0:
            return 'no more'
        else:
            return str(number)

    def container(self, number):
        if number == 1:
            return "bottle"
        else:
            return "bottles"

    def pronoun(self, number):
        if number == 1:
            return 'it'
        else:
            return 'one'

    def action(self, number):
        if number == 0:
            return "Go to the store and buy some more"
        else:
            return f"Take {self.pronoun(number)} down and pass it around"

    def successor(self, number):
        if number == 0:
            return 99
        else:
            return number - 1

class BottleNumber:
    def __init__(self, number):
        self.number = number
        self.quantity = self.set_quantity()
        self.container = self.set_container()
        self.action = self.set_action()
        self.successor = self.set_successor()

    def set_quantity(self):
        if self.number == 0:
            return "no more"
        else:
            return str(self.number)

    def set_container(self):
        if self.number == 1:
            return "bottle"
        else:
            return "bottles"

    def set_action(self):
        if self.number == 0:
            return "Go to the store and buy some more"
        else:
            return f"Take {self.pronoun()} down and pass it around"
    
    def pronoun(self):
        if self.number == 1:
            return 'it'
        else:
            return 'one'
    
    def set_successor(self):
        if self.number == 0:
            return 99
        else:
            return self.number - 1


if __name__ == '__main__':
    bottle = Bottles()
    print(bottle.song())