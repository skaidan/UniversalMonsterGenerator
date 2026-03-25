# bases1/swarm-of-cranium-rats.py
"""
SwarmOfCraniumRats creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-cranium-rats
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfCraniumRats(GlobalCreatureBaseClass):
    """
    Medium Swarm of Tiny aberrations creature - SwarmOfCraniumRats
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 14, 'CON': 10, 'INT': 15, 'WIS': 11, 'CHAR': 14, 'armor_class': 12, 'alignment': 'typically Lawful Evil Armor Class  12 Hit Points  76 (17d8) Speed  30 ft. STR 9 (-1) DEX 14 (+2) CON 10 (+0) INT 15 (+2) WIS 11 (+0) CHA 14 (+2) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'Swarm of Tiny aberrations', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

