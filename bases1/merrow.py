# bases1/merrow.py
"""
Merrow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merrow
"""
from creature_base import GlobalCreatureBaseClass


class Merrow(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Merrow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 15, 'INT': 8, 'WIS': 10, 'CHAR': 9, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 (natural armor) Hit Points  45 (6d10 + 12) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'claws', 'harpoon']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The merrow can breathe air and water."""
        return 'The merrow can breathe air and water.'

    def multiattack_attack(self) -> str:
        """The merrow makes two attacks: one with its bite and one with its claws or harpoon."""
        return 'The merrow makes two attacks: one with its bite and one with its claws or harpoon.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 9 (2d4 + 4) slashing damage.'

    def harpoon_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 11 (2d6 + 4) piercing damage. If the target is a Huge or smaller creature, it must succeed on a Strength contest against the merrow or be pulled up to 20 feet toward the merrow."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 11 (2d6 + 4) piercing damage. If the target is a Huge or smaller creature, it must succeed on a Strength contest against the merrow or be pulled up to 20 feet toward the merrow.'

