from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.robot_name=name
        self.robot_health=25
        self.active_weapon=Weapon(self, name)

    def attack(self, dinosaur):
        pass
