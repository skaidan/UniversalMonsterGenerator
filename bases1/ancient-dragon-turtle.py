# bases1/ancient-dragon-turtle.py
"""
AncientDragonTurtle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-dragon-turtle
"""
from creature_base import GlobalCreatureBaseClass


class AncientDragonTurtle(GlobalCreatureBaseClass):
    """
    Gargantuan Dragon creature - AncientDragonTurtle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 409, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 12, 'CON': 29, 'INT': 14, 'WIS': 19, 'CHAR': 15, 'armor_class': 22, 'alignment': 'typically Neutral Armor Class  22 (natural armor) Hit Points  409 (21d20 + 189) Speed  30 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

