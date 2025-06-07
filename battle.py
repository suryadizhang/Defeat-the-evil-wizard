from evilwizard import EvilWizard
from warrior import Warrior
from mage import Mage
from archer import Archer
from paladin import Paladin
from necromancer import Necromancer

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Restore Mana")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                print("a. Power Strike \nb. War Cry")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.power_strike(wizard)
                elif option == "b":
                    player.war_cry()
            elif isinstance(player, Mage):
                print("a. Fireball \nb. Mana Shield")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.fire_ball(wizard)
                elif option == "b":
                    player.mana_shield()
            elif isinstance(player, Archer):
                print("a. Quick Shot \nb. Evade")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.quick_shot(wizard)
                elif option == "b":
                    player.evade()
            elif isinstance(player, Paladin):
                print("a. Holy Strike \nb. Divine Shield")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.holy_strike(wizard)
                elif option == "b":
                    player.divine_shield()
            elif isinstance(player, Necromancer):
                print("a. Drain Life \nb. Raise Skeleton")
                option = input("Choose the ability: a or b ")
                if option == "a":
                    player.drain_life(wizard)
                elif option == "b":
                    player.raise_skeleton()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.restore_mana()
        elif choice == '5':
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