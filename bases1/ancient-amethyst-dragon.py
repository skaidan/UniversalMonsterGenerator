# bases1/ancient-amethyst-dragon.py
"""
AncientAmethystDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-amethyst-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientAmethystDragon(GlobalCreatureBaseClass):
    """
    Gargantuan dragon (Gem) creature - AncientAmethystDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 444, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 14, 'CON': 27, 'INT': 26, 'WIS': 19, 'CHAR': 23, 'armor_class': 20, 'alignment': 'typically Neutral Armor Class  20 (natural armor) Hit Points  444 (24d20 + 192) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

