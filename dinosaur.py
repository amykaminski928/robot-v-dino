class Dinosaur:
    def __init__(self, name, attack_power):
        self.dino_name=name
        self.dino_attack_power=attack_power
        self.dino_health=25

    def attack(self, robot):
        robot.robot_health-=self.dino_attack_power
        print (f'{robot.robot_name} has {robot.robot_health} health remaining.')