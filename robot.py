from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name=name
        self.robot_health=50
        self.active_weapon=Weapon("Fangs", 5)

    def attack(self, dinosaur):
        if self.robot_health > 0:
            print("Robot attacks.")
            dinosaur.dino_health-=self.active_weapon.weapon_attack_power
            print(f'{dinosaur.dino_name} has {dinosaur.dino_health} health remaining.')
        