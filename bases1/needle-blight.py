# bases1/needle-blight.py
"""
NeedleBlight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=needle-blight
"""
from creature_base import GlobalCreatureBaseClass


class NeedleBlight(GlobalCreatureBaseClass):
    """
    Medium plant creature - NeedleBlight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 12, 'CON': 13, 'INT': 4, 'WIS': 8, 'CHAR': 3, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 (natural armor) Hit Points  11 (2d8 + 2) Speed  30 ft. STR 12 (+1) DEX 12 (+1) CON 13 (+1) INT 4 (-3) WIS 8 (-1) CHA 3 (-4) Condition Immunities  blinded', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['claws', 'needles']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) piercing damage.'

    def needles_attack(self) -> str:
        """Ranged Weapon Attack: +3 to hit, range 30/60 ft., one target. Hit: 8 (2d6 + 1) piercing damage."""
        return 'Ranged Weapon Attack: +3 to hit, range 30/60 ft., one target. Hit: 8 (2d6 + 1) piercing damage.'

