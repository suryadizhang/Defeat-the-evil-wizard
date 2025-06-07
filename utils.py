from warrior import Warrior
from mage import Mage
from archer import Archer
from paladin import Paladin
from necromancer import Necromancer

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")
    print("5. Necromancer")

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
    elif class_choice == '5':
        return Necromancer(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)