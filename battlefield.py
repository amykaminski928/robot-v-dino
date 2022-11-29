from robot import Robot
from dinosaur import Dinosaur
#from weapon import Weapon

class Battlefield: 
    def __init__(self):
        self.active_robot=Robot("Chewy")
        self.active_dinosaur=Dinosaur("Blue",5)

    def run_game(self):
        Battlefield.display_welcome(self)
        Battlefield.battle_phase(self)
        Battlefield.display_winner(self)

    def display_welcome(self):
        print('Welcome to the superdome battle, Robot v. Dinosaur!')

    def battle_phase(self):
        #while Battlefield.active_robot > 0 or Dinosaur.dino_health > 0:
        #dinosaur.dino_health > 0 or Dinosaur.attack.robot.robot_health > 0:
        
        while self.active_dinosaur.dino_health > 0 and self.active_robot.robot_health > 0:
                
                self.active_robot.attack(self.active_dinosaur)
                
                self.active_dinosaur.attack(self.active_robot)
            #elif self.active_dinosaur.dino_health or self.active_robot.robot_health <= 0:
                

    def display_winner(self):
        if self.active_robot.robot_health <= 0:
            print("Dinosaur wins!")
        elif self.active_dinosaur.dino_health <= 0: 
            print("Robot wins!")