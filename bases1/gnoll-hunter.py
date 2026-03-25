# bases1/gnoll-hunter.py
"""
GnollHunter creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll-hunter
"""
from creature_base import GlobalCreatureBaseClass


class GnollHunter(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - GnollHunter
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 12, 'INT': 8, 'WIS': 12, 'CHAR': 8, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 (leather armor) Hit Points  22 (4d8 + 4) Speed  30 ft. STR 14 (+2) DEX 14 (+2) CON 12 (+1) INT 8 (-1) WIS 12 (+1) CHA 8 (-1) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'bite', 'spear', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The gnoll makes two Bite, Spear, or Longbow attacks."""
        return 'The gnoll makes two Bite, Spear, or Longbow attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage when used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 5 (1d6 + 2) piercing damage, or 6 (1d8 + 2) piercing damage when used with two hands to make a melee attack.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage, and the target's speed is reduced by 10 feet until the end of its next turn."""
        return "Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage, and the target's speed is reduced by 10 feet until the end of its next turn."

