from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        active_robot=Robot()
        active_dinosaur=Dinosaur()

    def run_game(self):
        pass

    def display_welcome(self):
        print('Welcome to the superdome battle, Robot v. Dinosaur!')

    def battle_phase(self):
        while Dinosaur.dino_health > 0 or Robot.robot_health > 0:
            print("Robot attacks.")
            Robot.attack
            print("Dinosaur retaliates.")
            Dinosaur.attack
       
    def display_winner(self):
        if Robot.robot_health <= 0:
            print("Dinosaur wins!")
        elif Dinosaur.dino_health <= 0: 
            print("Robot wins!")