# bases1/martial-arts-adept.py
"""
MartialArtsAdept creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=martial-arts-adept
"""
from creature_base import GlobalCreatureBaseClass


class MartialArtsAdept(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - MartialArtsAdept
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 17, 'CON': 13, 'INT': 11, 'WIS': 16, 'CHAR': 10, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (Unarmored Defense) Hit Points  60 (11d8 + 11) Speed  40 ft. STR 11 (+0) DEX 17 (+3) CON 13 (+1) INT 11 (+0) WIS 16 (+3) CHA 10 (+0) Skills  Acrobatics +5', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['unarmored_defense', 'multiattack', 'unarmed_strike', '&nbsp;_1–2', '&nbsp;_3–4', 'dart']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def unarmored_defense(self) -> str:
        """While the adept is wearing no armor and wielding no shield, its AC includes its Wisdom modifier."""
        return 'While the adept is wearing no armor and wielding no shield, its AC includes its Wisdom modifier.'

    def multiattack_attack(self) -> str:
        """The adept makes three Unarmed Strike attacks or five Dart attacks."""
        return 'The adept makes three Unarmed Strike attacks or five Dart attacks.'

    def unarmed_strike_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage. Once per turn, the adept can cause one of the following additional effects (choose one or roll a d4):"""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage. Once per turn, the adept can cause one of the following additional effects (choose one or roll a d4):'

    def &nbsp;_1–2_attack(self) -> str:
        """Knock Down-The target must succeed on a DC 13 Dexterity saving throw or be knocked prone."""
        return 'Knock Down-The target must succeed on a DC 13 Dexterity saving throw or be knocked prone.'

    def &nbsp;_3–4_attack(self) -> str:
        """Push-The target must succeed on a DC 13 Strength saving throw or be pushed up to 10 feet directly away from the adept."""
        return 'Push-The target must succeed on a DC 13 Strength saving throw or be pushed up to 10 feet directly away from the adept.'

    def dart_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 20/60 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

