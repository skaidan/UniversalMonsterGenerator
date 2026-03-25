# bases1/swarm-of-rot-grubs.py
"""
SwarmOfRotGrubs creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=swarm-of-rot-grubs
"""
from creature_base import GlobalCreatureBaseClass


class SwarmOfRotGrubs(GlobalCreatureBaseClass):
    """
    Medium swarm of Tiny beasts creature - SwarmOfRotGrubs
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 7, 'CON': 10, 'INT': 1, 'WIS': 2, 'CHAR': 1, 'armor_class': 8, 'alignment': 'unaligned Armor Class  8 Hit Points  22 (5d8) Speed  5 ft.', 'legendary': False, 'size': 'Medium', 'type': 'swarm of Tiny beasts', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

