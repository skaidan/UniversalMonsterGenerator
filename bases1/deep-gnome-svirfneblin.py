# bases1/deep-gnome-svirfneblin.py
"""
DeepGnomeSvirfneblin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deep-gnome-svirfneblin
"""
from creature_base import GlobalCreatureBaseClass


class DeepGnomeSvirfneblin(GlobalCreatureBaseClass):
    """
    DeepGnomeSvirfneblin creature
    Size: Small, Type: humanoid (Gnome), neutral good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 16,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "humanoid (Gnome), neutral good",
        "hit_points_up": [1, 1, 1],
        "STR_up": [1, 0, 0],
        "DEX_up": [1, 0, 0],
        "CON_up": [0, 1, 0],
        "INT_up": [0, 1, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 1],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.extend(['stone_camouflage'])

    def stone_camouflage(self) -> str:
        """Stone Camouflage: The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.Gnome Cunning. T..."""
        return "The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.Gnome Cunning. The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic.Innate Spel"
    def stone_camouflage(self) -> str:
        """Stone Camouflage: The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.Gnome Cunning. T..."""
        return "The gnome has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.Gnome Cunning. The gnome has advantage on Intelligence, Wisdom, and Charisma saving throws against magic.Innate Spel"

