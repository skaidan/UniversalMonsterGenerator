# bases1/ancient-crystal-dragon.py
"""
AncientCrystalDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-crystal-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientCrystalDragon(GlobalCreatureBaseClass):
    """
    Gargantuan dragon (Gem) creature - AncientCrystalDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 222, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 12, 'CON': 26, 'INT': 20, 'WIS': 16, 'CHAR': 21, 'armor_class': 20, 'alignment': 'typically Chaotic Neutral Armor Class  20 (natural armor) Hit Points  222 (12d20 + 96) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

