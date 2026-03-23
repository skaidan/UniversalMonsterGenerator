# bases1/water-weird.py
"""
WaterWeird creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=water-weird
"""
from creature_base import GlobalCreatureBaseClass


class WaterWeird(GlobalCreatureBaseClass):
    """
    WaterWeird creature
    Size: Medium, Type: or smaller, it is grappled (escape DC 13) and pulled 5 feet toward the water weird. Until this grapple ends, the target is restrained, the water weird tries to drown it, and the water weird can't constrict another target.
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 58,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, it is grappled (escape DC 13) and pulled 5 feet toward the water weird. Until this grapple ends, the target is restrained, the water weird tries to drown it, and the water weird can't constrict another target.",
        "hit_points_up": [5, 5, 5],
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
        self.abilities.extend(['invisible_in_water'])

    def invisible_in_water(self) -> str:
        """Invisible in Water: The water weird is invisible while fully immersed in water.Water Bound. The water weird dies if it l..."""
        return "The water weird is invisible while fully immersed in water.Water Bound. The water weird dies if it leaves the water to which it is bound or if that water is destroyed.ActionsConstrict. Melee Weapon At"
    def invisible_in_water(self) -> str:
        """Invisible in Water: The water weird is invisible while fully immersed in water.Water Bound. The water weird dies if it l..."""
        return "The water weird is invisible while fully immersed in water.Water Bound. The water weird dies if it leaves the water to which it is bound or if that water is destroyed.ActionsConstrict. Melee Weapon At"

