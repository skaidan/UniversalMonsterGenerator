# bases1/marilith.py
"""
Marilith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=marilith
"""
from creature_base import GlobalCreatureBaseClass


class Marilith(GlobalCreatureBaseClass):
    """
    Marilith creature
    Size: Medium, Type: or smaller, it is grappled (escape DC 19). Until this grapple ends, the target is restrained, the marilith can automatically hit the target with its tail, and the marilith can't make tail attacks against other targets.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 189,
        "min_level": 17,
        "level": 17,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it is grappled (escape DC 19). Until this grapple ends, the target is restrained, the marilith can automatically hit the target with its tail, and the marilith can't make tail attacks against other targets.",
        "hit_points_up": [18, 18, 18],
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The marilith has advantage on saving throws against spells and other magical effects.Magic Weapons. ..."""
        return "The marilith has advantage on saving throws against spells and other magical effects.Magic Weapons. The marilith's weapon attacks are magical.Reactive. The marilith can take one reaction on every turn"
    def magic_resistance(self) -> str:
        """Magic Resistance: The marilith has advantage on saving throws against spells and other magical effects.Magic Weapons. ..."""
        return "The marilith has advantage on saving throws against spells and other magical effects.Magic Weapons. The marilith's weapon attacks are magical.Reactive. The marilith can take one reaction on every turn"

