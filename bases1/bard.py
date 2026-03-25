# bases1/bard.py
"""
Bard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bard
"""
from creature_base import GlobalCreatureBaseClass


class Bard(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Bard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 44, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 13, 'CHAR': 14, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (chain shirt) Hit Points  44 (8d8 + 8) Speed  30 ft. STR 11 (+0) DEX 14 (+2) CON 12 (+1) INT 10 (+0) WIS 13 (+1) CHA 14 (+2) Saving Throws  Dex +4', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'shortsword', 'shortbow', 'cacophony_(recharge_4–6)', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The bard makes two Shortsword or Shortbow attacks. It can replace one attack with a use of Spellcasting."""
        return 'The bard makes two Shortsword or Shortbow attacks. It can replace one attack with a use of Spellcasting.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 80/320 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def cacophony_(recharge_4–6)_attack(self) -> str:
        """Each creature in a 15-foot cube originating from the bard must make a DC 12 Constitution saving throw. On a failed save, a creature takes 9 (2d8) thunder damage and is pushed up to 10 feet away from the bard. On a successful save, a creature takes half as much damage and isn't pushed."""
        return "Each creature in a 15-foot cube originating from the bard must make a DC 12 Constitution saving throw. On a failed save, a creature takes 9 (2d8) thunder damage and is pushed up to 10 feet away from the bard. On a successful save, a creature takes half as much damage and isn't pushed."

    def spellcasting_attack(self) -> str:
        """The bard casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):"""
        return 'The bard casts one of the following spells, using Charisma as the spellcasting ability (spell save DC 12):'

