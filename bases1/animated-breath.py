# bases1/animated-breath.py
"""
AnimatedBreath creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=animated-breath
"""
from creature_base import GlobalCreatureBaseClass


class AnimatedBreath(GlobalCreatureBaseClass):
    """
    Large Elemental creature - AnimatedBreath
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 95, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 11, 'CON': 18, 'INT': 6, 'WIS': 10, 'CHAR': 5, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) or 17 (Cold form only) Hit Points  95 (10d10 + 40) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

