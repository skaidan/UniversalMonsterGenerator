# bases1/manes.py
"""
Manes creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=manes
"""
from creature_base import GlobalCreatureBaseClass


class Manes(GlobalCreatureBaseClass):
    """
    Small fiend (Demon) creature - Manes
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 9, 'CON': 13, 'INT': 3, 'WIS': 8, 'CHAR': 4, 'armor_class': 9, 'alignment': 'chaotic evil Armor Class  9 Hit Points  9 (2d6 + 2) Speed  20 ft. STR 10 (+0) DEX 9 (-1) CON 13 (+1) INT 3 (-4) WIS 8 (-1) CHA 4 (-3) Damage Resistances  cold', 'legendary': False, 'size': 'Small', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) slashing damage.'

