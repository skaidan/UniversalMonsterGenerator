# bases1/tiamat.py
"""
Tiamat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tiamat
"""
from creature_base import GlobalCreatureBaseClass


class Tiamat(GlobalCreatureBaseClass):
    """
    Tiamat creature
    Size: Gargantuan, Type: fiend, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 615,
        "min_level": 31,
        "level": 31,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 25,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "fiend, chaotic evil",
        "hit_points_up": [61, 61, 61],
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
        # Add creature-specific abilities
        self.abilities.extend(['discorporation'])

    def discorporation(self) -> str:
        """Discorporation: When Tiamat drops to 0 hit points or dies, her body is destroyed but her essence travels back to her..."""
        return "When Tiamat drops to 0 hit points or dies, her body is destroyed but her essence travels back to her domain in the Nine Hells, and she is unable to take physical form for a time.Innate Spellcasting (3"

