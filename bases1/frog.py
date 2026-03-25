# bases1/frog.py
"""
Frog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frog
"""
from creature_base import GlobalCreatureBaseClass


class Frog(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Frog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 13, 'CON': 8, 'INT': 1, 'WIS': 8, 'CHAR': 3, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  1 (1d4 - 1) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The frog can breathe air and water.Standing Leap. The frog's long jump is up to 10 feet and its high jump is up to 5 feet, with or without a running start.A frog has no effective attacks. It feeds on """
        return "The frog can breathe air and water.Standing Leap. The frog's long jump is up to 10 feet and its high jump is up to 5 feet, with or without a running start.A frog has no effective attacks. It feeds on "

