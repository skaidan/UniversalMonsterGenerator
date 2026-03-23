# bases1/stone-golem.py
"""
StoneGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-golem
"""
from creature_base import GlobalCreatureBaseClass


class StoneGolem(GlobalCreatureBaseClass):
    """
    StoneGolem creature
    Size: Large, Type: construct, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 178,
        "min_level": 11,
        "level": 11,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "construct, unaligned",
        "hit_points_up": [17, 17, 17],
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
        self.abilities.extend(['immutable_form'])

    def immutable_form(self) -> str:
        """Immutable Form: The golem is immune to any spell or effect that would alter its form.Magic Resistance. The golem has..."""
        return "The golem is immune to any spell or effect that would alter its form.Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.Magic Weapons. The golem's weap"
    def immutable_form(self) -> str:
        """Immutable Form: The golem is immune to any spell or effect that would alter its form.Magic Resistance. The golem has..."""
        return "The golem is immune to any spell or effect that would alter its form.Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.Magic Weapons. The golem's weap"

