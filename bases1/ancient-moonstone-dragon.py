# bases1/ancient-moonstone-dragon.py
"""
AncientMoonstoneDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-moonstone-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientMoonstoneDragon(GlobalCreatureBaseClass):
    """
    Gargantuan dragon creature - AncientMoonstoneDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 330, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 18, 'CON': 23, 'INT': 20, 'WIS': 22, 'CHAR': 26, 'armor_class': 20, 'alignment': 'typically Neutral Armor Class  20 (natural armor) Hit Points  330 (20d20 + 120) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

