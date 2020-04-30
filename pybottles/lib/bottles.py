class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self, upper, lower):
        return '\n'.join([self.verse(i) for i in range(upper, lower-1, -1)])

    def verse(self, number):
        return f"{self.amount(number).capitalize()} {self.container(number)} of beer on the wall, " \
        f"{self.amount(number)} {self.container(number)} of beer.\n"\
        f"{self.action(number)}, "\
        f"{self.amount(self.successor(number))} {self.container(self.successor(number))} of beer on the wall.\n"

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

if __name__ == '__main__':
    bottle = Bottles()
    print(bottle.song())