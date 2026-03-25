# bases1/hobgoblin-iron-shadow.py
"""
HobgoblinIronShadow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-iron-shadow
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinIronShadow(GlobalCreatureBaseClass):
    """
    Medium Fey (Goblinoid) creature - HobgoblinIronShadow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 16, 'CON': 15, 'INT': 14, 'WIS': 15, 'CHAR': 11, 'armor_class': 15, 'alignment': 'typically Lawful Neutral Armor Class  15 (Unarmored Defense) Hit Points  32 (5d8 + 10) Speed  40 ft. STR 14 (+2) DEX 16 (+3) CON 15 (+2) INT 14 (+2) WIS 15 (+2) CHA 11 (+0) Skills  Acrobatics +5', 'legendary': False, 'size': 'Medium', 'type': 'Fey (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['unarmored_defense', 'multiattack', 'unarmed_strike', 'dart', 'shadow_jaunt', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def unarmored_defense(self) -> str:
        """While the hobgoblin is wearing no armor and wielding no shield, its AC includes its Wisdom modifier."""
        return 'While the hobgoblin is wearing no armor and wielding no shield, its AC includes its Wisdom modifier.'

    def multiattack_attack(self) -> str:
        """The hobgoblin makes four attacks, each of which can be an Unarmed Strike or a Dart attack. It can also use Shadow Jaunt once, either before or after one of the attacks."""
        return 'The hobgoblin makes four attacks, each of which can be an Unarmed Strike or a Dart attack. It can also use Shadow Jaunt once, either before or after one of the attacks.'

    def unarmed_strike_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage.'

    def dart_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

    def shadow_jaunt_attack(self) -> str:
        """The hobgoblin teleports, along with any equipment it is wearing or carrying, up to 30 feet to an unoccupied space it can see. Both the space it leaves and its destination must be in dim light or darkness."""
        return 'The hobgoblin teleports, along with any equipment it is wearing or carrying, up to 30 feet to an unoccupied space it can see. Both the space it leaves and its destination must be in dim light or darkness.'

    def spellcasting_attack(self) -> str:
        """The hobgoblin casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 12):"""
        return 'The hobgoblin casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 12):'

