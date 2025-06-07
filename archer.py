from character import Character
import random

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25, mana=30, speed=30, luck=20, defense=5)
        self.evade_next = False

    def quick_shot(self, opponent):
        mana_cost = 8
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Quick Shot!")
            return
        self.mana -= mana_cost
        print('Quick Shot! Arrow attack 2x')
        self.attack(opponent)
        if opponent.health > 0:
            self.attack(opponent)
        print(f"(Mana left: {self.mana}/{self.max_mana})")

    def evade(self):
        mana_cost = 7
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Evade!")
            return
        self.mana -= mana_cost
        self.evade_next = True
        print('Incoming attack evaded! (Evade active for next attack) (Mana left: {}/{})'.format(self.mana, self.max_mana))

    def receive_damage(self, damage):
        if self.evade_next:
            print(f'{self.name} evades the attack!')
            self.evade_next = False
        else:
            super().receive_damage(damage)