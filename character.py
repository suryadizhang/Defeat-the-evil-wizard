import random

class Character:
    def __init__(self, name, health, attack_power, mana, speed, luck, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.mana = mana
        self.max_mana = mana
        self.speed = speed
        self.luck = luck
        self.defense = defense

    def attack(self, opponent):
        #luck give small bonus damage
        luck_bonus = random.randint(0, int(self.luck / 10))
        min_attack = max(1, self.attack_power - 5)
        damage = random.randint(min_attack, self.attack_power + 5) + luck_bonus
        #luck give chance of critical damage
        critical = random.random() < (self.luck / 100)
        if critical:
            damage *= 2
            print('CRITICAL HIT!')
        opponent.receive_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def receive_damage(self, damage):
        #speed will give chance for dodge
        dodge = random.random() < (self.speed / 100)
        if dodge:
            print(f"{self.name} dodges the attack with a speedy move!")
        else:
            reduced_damage = max(0, damage - self.defense)
            self.health -= reduced_damage
            print(f"{self.name} receives {reduced_damage} damage, {self.defense} reduced from {damage} possible damage")
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Mana: {self.mana}/{self.max_mana}, "
              f"Attack Power: {self.attack_power}, Defense: {self.defense}, Speed: {self.speed}, Luck: {self.luck}")

    def heal(self):
        healed = int(0.2 * self.max_health)
        mana_cost = 15
        if self.mana < mana_cost:
            print(f"{self.name} does not have enough mana!")
            return
        self.mana -= mana_cost
        before = self.health
        self.health = min(self.max_health, self.health + healed)
        print(f'{self.name} heals for {self.health - before} HP (Mana left: {self.mana}/{self.max_mana})')

    def restore_mana(self):
        restored = int(0.25 * self.max_mana)
        before = self.mana
        self.mana = min(self.max_mana, self.mana + restored)
        print(f"{self.name} meditates and restores {self.mana - before} mana! (Mana left: {self.mana}/{self.max_mana})")