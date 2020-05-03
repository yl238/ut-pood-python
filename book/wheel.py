class Wheel(object):
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


class Gear(object):
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire= tire

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * Wheel(self.rim, self.tire).diameter()


if __name__ == '__main__':
    print(Gear(52,11, 26, 1.5).gear_inches())



