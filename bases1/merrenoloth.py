# bases1/merrenoloth.py
"""
Merrenoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=merrenoloth
"""
from creature_base import GlobalCreatureBaseClass


class Merrenoloth(GlobalCreatureBaseClass):
    """
    Medium Fiend (Yugoloth) creature - Merrenoloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 17, 'CON': 10, 'INT': 17, 'WIS': 14, 'CHAR': 11, 'armor_class': 13, 'alignment': 'typically Neutral Evil Armor Class  13 Hit Points  40 (9d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'multiattack', 'oar', 'fear_gaze', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The merrenoloth has advantage on saving throws against spells and other magical effects."""
        return 'The merrenoloth has advantage on saving throws against spells and other magical effects.'

    def multiattack_attack(self) -> str:
        """The merrenoloth makes one Oar attack and uses Fear Gaze."""
        return 'The merrenoloth makes one Oar attack and uses Fear Gaze.'

    def oar_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) fire damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (2d4 + 3) fire damage.'

    def fear_gaze_attack(self) -> str:
        """The merrenoloth targets one creature it can see within 60 feet of it. The target must succeed on a DC 13 Wisdom saving throw or become frightened of the merrenoloth for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The merrenoloth targets one creature it can see within 60 feet of it. The target must succeed on a DC 13 Wisdom saving throw or become frightened of the merrenoloth for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def spellcasting_attack(self) -> str:
        """The merrenoloth casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 13):"""
        return 'The merrenoloth casts one of the following spells, requiring no material components and using Intelligence as the spellcasting ability (spell save DC 13):'

