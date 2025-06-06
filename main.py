import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, mana, speed, luck):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        #make attack damage random within a range of 5 from the attack power
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.receive_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def receive_damage(self, damage):
        self.health -= damage

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    def heal(self):
        #healing will not exceed max_health
        healed = int(0.2 * self.max_health)
        before = self.health
        self.health = min(self.max_health, self.health + healed)
        print(f'{self.name} heals for {self.health - before} HP')

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.war_cry_active = False
        self.war_cry_turns = 0
        
    def power_strike(self, opponent):
        #power strike will deal damage between 1.3 to 1.7 of the initial attack power
        damage = random.randint(int(self.attack_power * 1.3), int(self.attack_power * 1.7))
        opponent.health -= damage
        print(f'{self.name} uses power strike! deal {damage} damage to {opponent.name}')
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
        
    # War cry raises damage for the next 2 turns
    def war_cry(self):
        self.war_cry_active = True
        self.war_cry_turns = 2
        print(f"{self.name} uses War Cry! Attack power increased for 2 turns.")
        
    def attack(self, opponent):
        if self.war_cry_active and self.war_cry_turns > 0:
            damage = int(self.attack_power * 1.3)
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage! (War Cry)")
            self.war_cry_turns -= 1
            if self.war_cry_turns == 0:
                self.war_cry_active = False
        else:
            super().attack(opponent)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.mana_shield_active = False
        self.mana_shield_turns = 0
    
    def fire_ball(self, opponent):
        damage = random.randint(int(self.attack_power* 1.2), int(self.attack_power * 1.6))
        opponent.health -= damage
        print(f'{self.name} cast Fireball on {opponent.name} dealt {damage} damage')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated')
            
    def mana_shield(self):
        self.mana_shield_active = True
        self.mana_shield_turns = 2
        print(f'{self.name} activated the mana shield. Incoming damage will be reduced by 25% for the next 2 turns.')
        
    def receive_damage(self, damage):
        if self.mana_shield_active and self.mana_shield_turns > 0:
            reduced = int(damage * 0.75)
            print(f'{self.name} activates mana shield reduces damage from {damage} to {reduced}')
            damage = reduced
            self.mana_shield_turns -= 1
            if self.mana_shield_turns == 0:
                self.mana_shield_active = False
        super().receive_damage(damage)
        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        before = self.health
        self.health = min(self.max_health, self.health +5)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        self.evade_next = False
    #quick_shot = double arrow attack
    def quick_shot(self, opponent):
        self.attack(opponent)
        #if the opponent died on the 1st attack the second attack wont happen else it will attack twice
        if opponent.health > 0: 
            self.attack(opponent)
        
    #Evade the next attack
    def evade(self):
        self.evade_next = True
        print ('incoming attack evaded')
        
    def receive_damage(self, damage):
        if self.evade_next:
            print(f'{self.name} evades the attack!')
            self.evade_next = False
        else:
            super().receive_damage(damage)            
        

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=10)
        self.shielded = False
        
    #Holy strike = bonus damage depend on current health *0.1
    def Holy_Strike(self, opponent):
        bonus = int(self.health * 0.1)
        damage = self.attack_power + bonus
        opponent.receive_damage(damage)
        print(f'Holy Strike activated! {self.name} deals {damage} damage to {opponent.name}')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
    
    def divine_shield(self):
        self.shielded = True
        print('Divine shield activated next attack will be blocked!')
        
    def receive_damage(self, damage):
        if self.shielded:
            print(f"{self.name}'s Divine shield blocked the attack")
        else:
            super().receive_damage(damage)

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Implement special abilities
            if isinstance(player, Warrior):
                print("a. Power Strike \nb. War Cry")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.power_strike(wizard)
                elif option == "b":
                    player.war_cry()
            if isinstance(player, Mage):
                print("a. Fireball \nb. Mana Shield")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.fire_ball(wizard)
                elif option == "b":
                    player.mana_shield()
            if isinstance(player, Archer):
                print("a. Quick Shot \nb. Evade")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.quick_shot(wizard)
                elif option == "b":
                    player.evade()
            if isinstance(player, Paladin):
                print("a. Holy Strike \nb. Divine Shield")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.Holy_Strike(wizard)
                elif option == "b":
                    player.divine_shield()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        print("VICTORY!!")
    elif player.health <= 0:
        print(f"{player.name} has fallen. Evil Wizard wins! ")
        print("GAME OVER!!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
