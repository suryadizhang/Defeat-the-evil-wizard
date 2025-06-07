from character import Character
import random

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, mana=30, speed=15, luck=10, defense=8)
        self.war_cry_active = False
        self.war_cry_turns = 0

    def power_strike(self, opponent):
        mana_cost = 10
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Power Strike!")
            return
        self.mana -= mana_cost
        damage = random.randint(int(self.attack_power * 1.3), int(self.attack_power * 1.7))
        opponent.receive_damage(damage)
        print(f'{self.name} uses Power Strike! Deals {damage} damage to {opponent.name} (Mana left: {self.mana}/{self.max_mana})')
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def war_cry(self):
        mana_cost = 8
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for War Cry!")
            return
        self.mana -= mana_cost
        self.war_cry_active = True
        self.war_cry_turns = 2
        print(f"{self.name} uses War Cry! Attack power increased for 2 turns. (Mana left: {self.mana}/{self.max_mana})")

    def attack(self, opponent):
        if self.war_cry_active and self.war_cry_turns > 0:
            damage = random.randint(int(self.attack_power * 1.2), int(self.attack_power * 1.5))
            opponent.receive_damage(damage)
            print(f"{self.name} attacks {opponent.name} for {damage} damage! (War Cry)")
            self.war_cry_turns -= 1
            if self.war_cry_turns == 0:
                self.war_cry_active = False
        else:
            super().attack(opponent)