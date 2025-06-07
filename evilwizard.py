from character import Character
import random

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, mana=40, speed=10, luck=12, defense=6)
        self.minion_turns = 0

    def summon_minion(self):
        self.minion_turns = 2
        print(f"{self.name} summons a dark minion! The minion will absorb damage for 2 turns.")

    def dark_blast(self, opponent):
        if self.mana < 10:
            self.mana += 5  # recover mana if not enough
            self.attack(opponent)
            return
        self.mana -= 10
        damage = random.randint(25, 40)
        opponent.receive_damage(damage)
        print(f"{self.name} uses DARK BLAST! Deals {damage} damage to {opponent.name}!")

    def attack(self, opponent):
        # If minion is up, absorb the attack intended for the wizard
        if self.minion_turns > 0:
            print(f"A minion absorbs all attacks for {self.name}!")
            self.minion_turns -= 1
        else:
            # Randomly choose action
            action = random.choices(
                ['attack', 'dark_blast', 'summon_minion'],
                weights=[0.6, 0.3, 0.1]
            )[0]
            if action == 'attack':
                super().attack(opponent)
            elif action == 'dark_blast':
                self.dark_blast(opponent)
            elif action == 'summon_minion':
                self.summon_minion()

    def regenerate(self):
        before = self.health
        self.health = min(self.max_health, self.health + 5)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")