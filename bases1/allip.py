# bases1/allip.py
"""
Allip creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=allip
"""
from creature_base import GlobalCreatureBaseClass


class Allip(GlobalCreatureBaseClass):
    """
    Medium Undead creature - Allip
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 17, 'CON': 10, 'INT': 17, 'WIS': 15, 'CHAR': 16, 'armor_class': 13, 'alignment': 'typically Neutral Evil Armor Class  13 Hit Points  40 (9d8) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['incorporeal_movement', 'maddening_touch', 'howling_babble_(recharge_6)', 'whispers_of_compulsion']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def incorporeal_movement(self) -> str:
        """The allip can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Unusual Nature. The allip doesn't require """
        return "The allip can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Unusual Nature. The allip doesn't require "

    def maddening_touch_attack(self) -> str:
        """Melee Spell Attack: +6 to hit, reach 5 ft., one target. Hit: 17 (4d6 + 3) psychic damage."""
        return 'Melee Spell Attack: +6 to hit, reach 5 ft., one target. Hit: 17 (4d6 + 3) psychic damage.'

    def howling_babble_(recharge_6)_attack(self) -> str:
        """Each creature within 30 feet of the allip that can hear it must make a DC 14 Wisdom saving throw. On a failed save, a target takes 12 (2d8 + 3) psychic damage, and it is stunned until the end of its next turn. On a successful save, it takes half as much damage and isn't stunned. Constructs and Undead are immune to this effect."""
        return "Each creature within 30 feet of the allip that can hear it must make a DC 14 Wisdom saving throw. On a failed save, a target takes 12 (2d8 + 3) psychic damage, and it is stunned until the end of its next turn. On a successful save, it takes half as much damage and isn't stunned. Constructs and Undead are immune to this effect."

    def whispers_of_compulsion_attack(self) -> str:
        """The allip chooses up to three creatures it can see within 60 feet of it. Each target must succeed on a DC 14 Wisdom saving throw, or it takes 12 (2d8 + 3) psychic damage and must use its reaction to make a melee weapon attack against one creature of the allip's choice that the allip can see. Constructs and Undead are immune to this effect."""
        return "The allip chooses up to three creatures it can see within 60 feet of it. Each target must succeed on a DC 14 Wisdom saving throw, or it takes 12 (2d8 + 3) psychic damage and must use its reaction to make a melee weapon attack against one creature of the allip's choice that the allip can see. Constructs and Undead are immune to this effect."

