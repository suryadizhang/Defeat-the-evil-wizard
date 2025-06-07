# Wizard Battle RPG

A simple, turn-based, console RPG written in Python. Choose a hero class, fight the Evil Wizard, and use unique abilities, mana, speed, luck, and defense to win!  
This project demonstrates object-oriented programming, randomness, and modular code.

---

## Features

- **Playable Classes:** Warrior, Mage, Archer, Paladin, Necromancer (each with unique mechanics and abilities)
- **Evil Wizard Boss:** Uses random advanced abilities, including powerful spells and summoning minions
- **Mana, Speed, Luck, Defense:** All stats affect gameplay
- **Restore Mana:** Meditate to regain mana during battle
- **Fully Modular:** Each class and function is split into its own `.py` file for clarity and maintainability

---

## How to Play

1. **Clone or download this repository.**
2. **Make sure you have Python 3 installed.**
3. **Run the game from the project directory:**
   ```sh
   python main.py
   ```
4. **Follow the prompts to:**
    - Choose your hero class and name
    - Use the menu each turn to attack, use special abilities, heal, restore mana, or view stats
    - Try to defeat the Evil Wizard and his minions!

---

## Project Structure

```
wizard_battle/
├── main.py           # Entry point for the game
├── character.py      # Base Character class
├── warrior.py        # Warrior class
├── mage.py           # Mage class
├── archer.py         # Archer class
├── paladin.py        # Paladin class
├── necromancer.py    # Necromancer class
├── evilwizard.py     # EvilWizard boss class
├── battle.py         # Main battle loop/logic
├── utils.py          # Character creation and utilities
└── README.md         # This file
```

---

## Class Abilities (Summary)

- **Warrior:** Power Strike, War Cry (buff)
- **Mage:** Fireball (high damage), Mana Shield (damage reduction)
- **Archer:** Quick Shot (double attack), Evade (dodge next hit)
- **Paladin:** Holy Strike (damage scales with health), Divine Shield (block next hit)
- **Necromancer:** Drain Life (damage/steal HP), Raise Skeleton (block attacks)
- **Evil Wizard:** Randomly attacks, casts Dark Blast, or summons a minion to absorb damage

---

## Customization and Expansion

- Add more classes or bosses by following the OOP pattern in the code
- Tweak the stats, balance abilities, or add new mechanics (cooldowns, criticals, items, etc.)
- Use this project as a learning base for larger game development in Python

---

## Credits

Created by suryadizhang
