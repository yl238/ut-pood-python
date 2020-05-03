class Wheel(object):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
        self.diameter = self.get_diameter()

    def get_diameter(self):
        return self.rim + (self.tire * 2)


class Gear(object):
    def __init__(self, chainring=None, cog=None, wheel=None):
        self.chainring = chainring or self.default_chainring()
        self.cog = cog
        self.wheel = wheel

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * self.diameter()

    def diameter(self):
        return self.wheel.diameter

    def default_chainring(self):
        return (100/2) - 10

if __name__ == '__main__':
    print(Gear(cog=11, wheel=Wheel(26, 1.5)).gear_inches())


