class ironMan:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = int(health_points)
        self.catchphrase = catchphrase
        self.damage = int(damage)
        self.fly = False

    def __str__(self):
        return f"{self.nickname}, {self.superpower}, {self.health_points}"

    def name_print(self):
        return self.name

    def nickname_print(self):
        return self.nickname

    def superpower_print(self):
        return self.superpower

    def health_points_print(self):
        self.fly = True
        return self.health_points ** 2

    def catchphrase_print(self):
        return self.catchphrase

    def __len__(self):
        return len(self.catchphrase)

    def true_phrase(self):
        return "True in the True_phrase"


class AirHero(ironMan):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.region = "Air"

class GroundHero(ironMan):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.region = "Ground"


class Villain(ironMan):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self):
        return self.damage ** 2


air_hero = AirHero("Airman", "sky walker", "control air",
                   "8000", "I rule the skies", "300")

ground_hero = GroundHero("Earthman", "ground breaker",
                         "control earth", "9000", "I am one with the earth", "400")

print(air_hero.health_points_print())
print(air_hero.fly)  # True
print(air_hero.true_phrase())

print(ground_hero.health_points_print())
print(ground_hero.fly)  # True
print(ground_hero.true_phrase())

villain = Villain("Doom", "night terror", "dark magic", "7000", "I bring the night", "500")

print(villain.crit())
