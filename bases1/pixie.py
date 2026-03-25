# bases1/pixie.py
"""
Pixie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pixie
"""
from creature_base import GlobalCreatureBaseClass


class Pixie(GlobalCreatureBaseClass):
    """
    Tiny fey creature - Pixie
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 20, 'CON': 8, 'INT': 10, 'WIS': 14, 'CHAR': 15, 'armor_class': 15, 'alignment': 'neutral good Armor Class  15 Hit Points  1 (1d4 - 1) Speed  10 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['magic_resistance', 'superior_invisibility']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def magic_resistance(self) -> str:
        """The pixie has advantage on saving throws against spells and other magical effects.Innate Spellcasting. The pixie's innate spellcasting ability is Charisma (spell save DC 12). It can innately cast the """
        return "The pixie has advantage on saving throws against spells and other magical effects.Innate Spellcasting. The pixie's innate spellcasting ability is Charisma (spell save DC 12). It can innately cast the "

    def superior_invisibility_attack(self) -> str:
        """The pixie magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the pixie wears or carries is invisible with it."""
        return 'The pixie magically turns invisible until its concentration ends (as if concentrating on a spell). Any equipment the pixie wears or carries is invisible with it.'

