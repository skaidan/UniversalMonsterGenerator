# bases1/yellow-musk-zombie.py
"""
YellowMuskZombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yellow-musk-zombie
"""
from creature_base import GlobalCreatureBaseClass


class YellowMuskZombie(GlobalCreatureBaseClass):
    """
    Medium undead creature - YellowMuskZombie
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 9, 'CON': 12, 'INT': 1, 'WIS': 6, 'CHAR': 3, 'armor_class': 9, 'alignment': 'unaligned Armor Class  9 Hit Points  33 (6d8 + 6) Speed  20 ft. STR 13 (+1) DEX 9 (-1) CON 12 (+1) INT 1 (-5) WIS 6 (-2) CHA 3 (-4) Condition Immunities  charmed', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

