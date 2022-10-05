import math


class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    def mix(self, other):
        self_color = [self.color[0]*self.volume, self.color[1]
                      * self.volume, self.color[2]*self.volume]
        other_color = [other.color[0]*other.volume, other.color[1]
                       * other.volume, other.color[2]*other.volume]
        new_volume = self.volume+other.volume
        new_color = [math.ceil((self_color[i] + other_color[i]) /
                     new_volume) for i in range(3)]

        new_potion = Potion(tuple(new_color), new_volume)
        return new_potion


felix_felicis = Potion((255, 255, 255),  7)
shrinking_solution = Potion((51, 102,  51), 12)

new_potion = felix_felicis.mix(shrinking_solution)

print(new_potion.color)
print(new_potion.volume)
