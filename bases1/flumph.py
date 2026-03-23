# bases1/flumph.py
"""
Flumph creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flumph
"""
from creature_base import GlobalCreatureBaseClass


class Flumph(GlobalCreatureBaseClass):
    """
    Flumph creature
    Size: Small, Type: aberration, lawful good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "aberration, lawful good",
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
        self.abilities.extend(['advanced_telepathy'])

    def advanced_telepathy(self) -> str:
        """Advanced Telepathy: The flumph can perceive the content of any telepathic communication used within 60 feet of it, and i..."""
        return "The flumph can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy.Prone Deficiency. If the flumph is knoc"
    def advanced_telepathy(self) -> str:
        """Advanced Telepathy: The flumph can perceive the content of any telepathic communication used within 60 feet of it, and i..."""
        return "The flumph can perceive the content of any telepathic communication used within 60 feet of it, and it can't be surprised by creatures with any form of telepathy.Prone Deficiency. If the flumph is knoc"

