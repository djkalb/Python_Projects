


class Organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    dna = "sequence a"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {} \nSpecies: {} \nLegs: {} \nArms: {} \ndna: {} \nOrigin: {} \nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg

class Human(Organism):
    name = "macguyver"
    species = "human"
    legs = 2
    arms = 2
    dna = 'sequence A'
    origin = "Earth"
    carbon_based = True

    def ingen(self):
        msg = "\nCreates weapons out of some materials."
        return msg
class Dog(Organism):
    name = "Spot"
    species= "Canine"
    legs = 4
    arms = 0
    dna = "sequence b"
    origin = "earth"

    def bite(self):
        msg = "\nthis is boring"
        return msg

class Bacterium(Organism):
    name = "X"
    species = "bacteria"
    legs = 0
    arms = 0
    dna = "sequence C"
    origin = "Mars"

    def repl(self):
        msg = "\nThe cells divide and reform i guess"
        return msg

    



if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingen())
    dog = Dog()
    print(dog.information())
    print(dog.bite())
    bacti = Bacterium()
    print(bacti.information())
    print(bacti.repl())
