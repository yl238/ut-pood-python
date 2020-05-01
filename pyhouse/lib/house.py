class House:
    def recite(self):
        return '\n'.join([self.line(i) for i in range(1, 13)])

    def phrase(self, number):
        return " ".join(["the horse and the hound and the horn that belonged to",
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
      ""][-number:])

    def line(self, number):
        return "This is " + self.phrase(number) + "the house that Jack built.\n"

if __name__ == '__main__':
    print(House().line(1))


    