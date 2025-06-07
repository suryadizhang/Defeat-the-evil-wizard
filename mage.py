from character import Character
import random

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, mana=60, speed=20, luck=15, defense=3)
        self.mana_shield_active = False
        self.mana_shield_turns = 0

    def fire_ball(self, opponent):
        mana_cost = 15
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Fireball!")
            return
        self.mana -= mana_cost
        damage = random.randint(int(self.attack_power * 1.2), int(self.attack_power * 1.6))
        opponent.receive_damage(damage)
        print(f'{self.name} casts Fireball on {opponent.name}, dealing {damage} damage (Mana left: {self.mana}/{self.max_mana})')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated')

    def mana_shield(self):
        mana_cost = 10
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Mana Shield!")
            return
        self.mana -= mana_cost
        self.mana_shield_active = True
        self.mana_shield_turns = 2
        print(f'{self.name} activates Mana Shield (Mana left: {self.mana}/{self.max_mana}). Incoming damage will be reduced by 25% for the next 2 turns.')

    def receive_damage(self, damage):
        if self.mana_shield_active and self.mana_shield_turns > 0:
            reduced = int(damage * 0.75)
            print(f'{self.name}\'s Mana Shield reduces damage from {damage} to {reduced}')
            damage = reduced
            self.mana_shield_turns -= 1
            if self.mana_shield_turns == 0:
                self.mana_shield_active = False
        super().receive_damage(damage)