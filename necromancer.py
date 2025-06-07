from character import Character
import random

class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20, mana=50, speed=18, luck=15, defense=5)
        self.skeleton_turns = 0

    def drain_life(self, opponent):
        mana_cost = 15
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana for Drain Life!")
            return
        self.mana -= mana_cost
        damage = random.randint(self.attack_power, self.attack_power + 15)
        opponent.receive_damage(damage)
        heal_amount = int(damage // 2)
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} drains {damage} HP from {opponent.name} and heals for {heal_amount} HP! (Mana left: {self.mana}/{self.max_mana})")

    def raise_skeleton(self):
        mana_cost = 20
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana to Raise Skeleton!")
            return
        self.mana -= mana_cost
        self.skeleton_turns = 2
        print(f"{self.name} summons a skeleton! All damage will be absorbed for the next 2 turns. (Mana left: {self.mana}/{self.max_mana})")

    def receive_damage(self, damage):
        if self.skeleton_turns > 0:
            print(f"A skeleton absorbs the attack for {self.name}!")
            self.skeleton_turns -= 1
        else:
            super().receive_damage(damage)