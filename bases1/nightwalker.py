# bases1/nightwalker.py
"""
Nightwalker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nightwalker
"""
from creature_base import GlobalCreatureBaseClass


class Nightwalker(GlobalCreatureBaseClass):
    """
    Nightwalker creature
    Size: Huge, Type: Undead, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 337,
        "min_level": 21,
        "level": 21,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Undead, typically Chaotic Evil",
        "hit_points_up": [33, 33, 33],
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
        self.abilities.extend(['annihilating_aura'])

    def annihilating_aura(self) -> str:
        """Annihilating Aura: Any creature that starts its turn within 30 feet of the nightwalker must succeed on a DC 21 Constitu..."""
        return "Any creature that starts its turn within 30 feet of the nightwalker must succeed on a DC 21 Constitution saving throw or take 21 (6d6) necrotic damage. Undead are immune to this aura.Life Eater. A cre"

