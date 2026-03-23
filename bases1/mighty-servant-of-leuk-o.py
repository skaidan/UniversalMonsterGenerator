# bases1/mighty-servant-of-leuk-o.py
"""
MightyServantOfLeukO creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mighty-servant-of-leuk-o
"""
from creature_base import GlobalCreatureBaseClass


class MightyServantOfLeukO(GlobalCreatureBaseClass):
    """
    MightyServantOfLeukO creature
    Size: Huge, Type: construct, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 310,
        "min_level": 1,
        "level": 1,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 22,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "construct, -",
        "hit_points_up": [31, 31, 31],
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
        self.abilities.extend(['immutable_existence'])

    def immutable_existence(self) -> str:
        """Immutable Existence: The servant is immune to any spell or effect that would alter its form or send it to another plane o..."""
        return "The servant is immune to any spell or effect that would alter its form or send it to another plane of existence.Magic Resistant Construction. The servant has advantage on saving throws against spells "

