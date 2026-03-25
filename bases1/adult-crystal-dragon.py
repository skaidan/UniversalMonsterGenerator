# bases1/adult-crystal-dragon.py
"""
AdultCrystalDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-crystal-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultCrystalDragon(GlobalCreatureBaseClass):
    """
    Huge dragon (Gem) creature - AdultCrystalDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 172, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 12, 'CON': 21, 'INT': 18, 'WIS': 15, 'CHAR': 19, 'armor_class': 16, 'alignment': 'typically Chaotic Neutral Armor Class  16 (natural armor) Hit Points  172 (15d12 + 75) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

