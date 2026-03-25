# bases1/sea-horse.py
"""
SeaHorse creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sea-horse
"""
from creature_base import GlobalCreatureBaseClass


class SeaHorse(GlobalCreatureBaseClass):
    """
    Tiny beast creature - SeaHorse
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 12, 'CON': 8, 'INT': 1, 'WIS': 10, 'CHAR': 2, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  1 (1d4 - 1) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['water_breathing']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def water_breathing(self) -> str:
        """The sea horse can breathe only underwater.Monster Manual (SRD)
			
				
			    	DnD 5e Monsters › Sea Horse"""
        return 'The sea horse can breathe only underwater.Monster Manual (SRD)\n\t\t\t\n\t\t\t\t\n\t\t\t    \tDnD 5e Monsters › Sea Horse'

