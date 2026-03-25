# bases1/satyr.py
"""
Satyr creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=satyr
"""
from creature_base import GlobalCreatureBaseClass


class Satyr(GlobalCreatureBaseClass):
    """
    Medium fey creature - Satyr
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 31, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 11, 'INT': 12, 'WIS': 10, 'CHAR': 14, 'armor_class': 14, 'alignment': 'chaotic neutral Armor Class  14 (leather armor) Hit Points  31 (7d8) Speed  40 ft. STR 12 (+1) DEX 16 (+3) CON 11 (+0) INT 12 (+1) WIS 10 (+0) CHA 14 (+2) Skills  Perception +2', 'legendary': False, 'size': 'Medium', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'ram', 'shortsword', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The satyr has advantage on saving throws against spells and other magical effects."""
        return 'The satyr has advantage on saving throws against spells and other magical effects.'

    def ram_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) bludgeoning damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) bludgeoning damage.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 80/320 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

