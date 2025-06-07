from character import Character
import random

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=10, mana=40, speed=10, luck=10, defense=12)
        self.shielded = False

    def holy_strike(self, opponent):
        mana_cost = 12
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Holy Strike!")
            return
        self.mana -= mana_cost
        bonus = int(self.health * 0.1)
        damage = self.attack_power + bonus
        opponent.receive_damage(damage)
        print(f'Holy Strike activated! {self.name} deals {damage} damage to {opponent.name} (Mana left: {self.mana}/{self.max_mana})')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')

    def divine_shield(self):
        mana_cost = 10
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Divine Shield!")
            return
        self.mana -= mana_cost
        self.shielded = True
        print('Divine Shield activated! Next attack will be blocked. (Mana left: {}/{})'.format(self.mana, self.max_mana))

    def receive_damage(self, damage):
        if self.shielded:
            print(f"{self.name}'s Divine Shield blocks the attack!")
            self.shielded = False
        else:
            super().receive_damage(damage)